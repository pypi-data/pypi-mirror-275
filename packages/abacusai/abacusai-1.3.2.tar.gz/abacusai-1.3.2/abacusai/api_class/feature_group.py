import dataclasses
from typing import List

from . import enums
from .abstract import ApiClass, _ApiClassFactory


@dataclasses.dataclass
class SamplingConfig(ApiClass):
    """
    An abstract class for the sampling config of a feature group
    """
    sampling_method: enums.SamplingMethodType = dataclasses.field(default=None, repr=False, init=False)

    @classmethod
    def _get_builder(cls):
        return _SamplingConfigFactory

    def __post_init__(self):
        if self.__class__ == SamplingConfig:
            raise TypeError('Cannot instantiate abstract SamplingConfig class.')


@dataclasses.dataclass
class NSamplingConfig(SamplingConfig):
    """
    The number of distinct values of the key columns to include in the sample, or number of rows if key columns not specified.

    Args:
        sampling_method (SamplingMethodType): N_SAMPLING
        sample_count (int): The number of rows to include in the sample
        key_columns (List[str]): The feature(s) to use as the key(s) when sampling
    """
    sample_count: int
    key_columns: List[str] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self.sampling_method = enums.SamplingMethodType.N_SAMPLING


@dataclasses.dataclass
class PercentSamplingConfig(SamplingConfig):
    """
    The fraction of distinct values of the feature group to include in the sample.

    Args:
        sampling_method (SamplingMethodType): PERCENT_SAMPLING
        sample_percent (float): The percentage of the rows to sample
        key_columns (List[str]): The feature(s) to use as the key(s) when sampling
    """
    sample_percent: float
    key_columns: List[str] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self.sampling_method = enums.SamplingMethodType.PERCENT_SAMPLING


@dataclasses.dataclass
class _SamplingConfigFactory(_ApiClassFactory):
    config_class_key = 'sampling_method'
    config_abstract_class = SamplingConfig
    config_class_map = {
        enums.SamplingMethodType.N_SAMPLING: NSamplingConfig,
        enums.SamplingMethodType.PERCENT_SAMPLING: PercentSamplingConfig,
    }


@dataclasses.dataclass
class MergeConfig(ApiClass):
    """
    An abstract class for the merge config of a feature group
    """
    merge_mode: enums.MergeMode = dataclasses.field(default=None, repr=False, init=False)

    @classmethod
    def _get_builder(self):
        return _MergeConfigFactory

    def __post_init__(self):
        if self.__class__ == MergeConfig:
            raise TypeError('Cannot instantiate abstract MergeConfig class.')


@dataclasses.dataclass
class LastNMergeConfig(MergeConfig):
    """
    Merge LAST N chunks/versions of an incremental dataset.

    Args:
        merge_mode (MergeMode): LAST_N
        num_versions (int): The number of versions to merge. num_versions == 0 means merge all versions.
        include_version_timestamp_column (bool): If set, include a column with the creation timestamp of source FG versions.
    """
    num_versions: int
    include_version_timestamp_column: bool = dataclasses.field(default=None)

    def __post_init__(self):
        self.merge_mode = enums.MergeMode.LAST_N


@dataclasses.dataclass
class TimeWindowMergeConfig(MergeConfig):
    """
    Merge rows within a given timewindow of the most recent timestamp

    Args:
        merge_mode (MergeMode): TIME_WINDOW
        feature_name (str): Time based column to index on
        time_window_size_ms (int): Range of merged rows will be [MAX_TIME - time_window_size_ms, MAX_TIME]
        include_version_timestamp_column (bool): If set, include a column with the creation timestamp of source FG versions.
    """
    feature_name: str
    time_window_size_ms: int
    include_version_timestamp_column: bool = dataclasses.field(default=None)

    def __post_init__(self):
        self.merge_mode = enums.MergeMode.TIME_WINDOW


@dataclasses.dataclass
class _MergeConfigFactory(_ApiClassFactory):
    config_class_key = 'merge_mode'
    config_abstract_class = MergeConfig
    config_class_map = {
        enums.MergeMode.LAST_N: LastNMergeConfig,
        enums.MergeMode.TIME_WINDOW: TimeWindowMergeConfig,
    }
