"""Run the phenotype quantitative concentration data assignment.

Copyright (c) 2022 to present Mitja Maximilian Zdouc, PhD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging
from typing import Self

from pydantic import BaseModel
from scipy.stats import pearsonr, zscore

from fermo_core.data_processing.builder_feature.dataclass_feature import Phenotype
from fermo_core.data_processing.class_repository import Repository
from fermo_core.data_processing.class_stats import Stats
from fermo_core.input_output.class_parameter_manager import ParameterManager

logger = logging.getLogger("fermo_core")


class PhenQuantConcAssigner(BaseModel):
    """Pydantic-based class to run qualitative phenotype assignment on concentrat. data

    Attributes:
        params: ParameterManager object, holds user-provided parameters
        stats: Stats object, holds stats on molecular features and samples
        features: Repository object, holds "General Feature" objects
        samples: Repository object holding Sample objects
        relevant_f_ids: features detected in > 3 samples
    """

    params: ParameterManager
    stats: Stats
    features: Repository
    samples: Repository
    relevant_f_ids: set = set()

    def return_values(self: Self) -> tuple[Stats, Repository]:
        """Return the modified objects to the calling function

        Returns:
            The modified Stats and Repository objects
        """
        return self.stats, self.features

    def find_relevant_f_ids(self: Self):
        """Determines features detected in > 3 samples"""
        for f_id in self.stats.active_features:
            feature = self.features.get(f_id)
            if len(feature.samples) > 3:
                self.relevant_f_ids.add(f_id)
            else:
                logger.debug(
                    f"'PhenQuantConcAssigner': feature id '{f_id}' only detected in "
                    f"'{len(feature.samples)}' samples: exclude from correlation "
                    f"analysis."
                )

    def calculate_correlation(self: Self):
        """Collect data, transform, scale, calculate correlation, correct p-val, assign

        Raises:
            RuntimeError: No relevant features (present in >3 samples) detected.
        """
        if len(self.relevant_f_ids) == 0:
            raise RuntimeError(
                "'PhenQuantConcAssigner': No relevant features (detected in >3 "
                "samples) detected - SKIP."
            )

        for f_id in self.relevant_f_ids:
            feature = self.features.get(f_id)
            f_areas = {val.s_id: val.value for val in feature.area_per_sample}

            for num, assay in enumerate(self.stats.phenotypes):
                areas = []
                activs = []
                for s_id in feature.samples:
                    for measure in assay.s_phen_data:
                        if s_id == measure.s_id:
                            areas.append(f_areas[s_id])
                            activs.append(measure.value)

                if len(areas) < 3:
                    logger.debug(
                        f"'PhenQuantConcAssigner': feature id '{f_id}' only detected in"
                        f"two samples - pass."
                    )
                    continue

                activs_reciprocal = [(1 / val) if val != 0 else 0 for val in activs]

                areas_scaled = zscore(areas)
                activs_scaled = zscore(activs_reciprocal)

                pearson_s, p_val = pearsonr(areas_scaled, activs_scaled)

                p_val_cor = p_val * len(self.relevant_f_ids)
                if p_val_cor > 1.0:
                    p_val_cor = 1.0

                if (
                    self.params.PhenoQuantConcAssgnParams.coeff_cutoff == 0
                    or self.params.PhenoQuantConcAssgnParams.p_val_cutoff == 0
                ):
                    if feature.phenotypes is None:
                        feature.phenotypes = []
                    feature.phenotypes.append(
                        Phenotype(
                            format=assay.datatype,
                            category=assay.category,
                            score=pearson_s,
                            p_value=p_val,
                            p_value_corr=p_val_cor,
                        )
                    )
                    self.stats.phenotypes[num].f_ids_positive.add(f_id)
                elif (
                    pearson_s > self.params.PhenoQuantConcAssgnParams.coeff_cutoff
                    and p_val_cor < self.params.PhenoQuantConcAssgnParams.p_val_cutoff
                ):
                    if feature.phenotypes is None:
                        feature.phenotypes = []
                    feature.phenotypes.append(
                        Phenotype(
                            format=assay.datatype,
                            category=assay.category,
                            score=pearson_s,
                            p_value=p_val,
                            p_value_corr=p_val_cor,
                        )
                    )
                    self.stats.phenotypes[num].f_ids_positive.add(f_id)
                else:
                    continue

            self.features.modify(f_id, feature)

    def run_analysis(self: Self):
        """Run the phenotype annotation analysis

        Raise:
            RuntimeError: self.stats.phenotypes not assigned
        """
        if self.stats.phenotypes is None:
            raise RuntimeError(
                "'PhenQuantConcAssigner': self.stats.phenotypes not assigne - SKIP"
            )

        self.find_relevant_f_ids()
        self.calculate_correlation()
