# generated by datamodel-codegen:
#   filename:  configuration/profilerConfiguration.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ..entity.data import table


class MetricType(Enum):
    mean = 'mean'
    valuesCount = 'valuesCount'
    countInSet = 'countInSet'
    columnCount = 'columnCount'
    distinctCount = 'distinctCount'
    distinctProportion = 'distinctProportion'
    iLikeCount = 'iLikeCount'
    likeCount = 'likeCount'
    notLikeCount = 'notLikeCount'
    regexCount = 'regexCount'
    notRegexCount = 'notRegexCount'
    max = 'max'
    maxLength = 'maxLength'
    min = 'min'
    minLength = 'minLength'
    nullCount = 'nullCount'
    rowCount = 'rowCount'
    stddev = 'stddev'
    sum = 'sum'
    uniqueCount = 'uniqueCount'
    uniqueProportion = 'uniqueProportion'
    columnNames = 'columnNames'
    duplicateCount = 'duplicateCount'
    iLikeRatio = 'iLikeRatio'
    likeRatio = 'likeRatio'
    nullProportion = 'nullProportion'
    interQuartileRange = 'interQuartileRange'
    nonParametricSkew = 'nonParametricSkew'
    median = 'median'
    firstQuartile = 'firstQuartile'
    thirdQuartile = 'thirdQuartile'
    system = 'system'
    histogram = 'histogram'


class MetricConfigurationDefinition(BaseModel):
    class Config:
        extra = Extra.forbid

    dataType: Optional[table.DataType] = None
    metrics: Optional[List[MetricType]] = None
    disabled: Optional[bool] = Field(
        False, description='If true, the metric will not be computed for the data type.'
    )


class ProfilerConfiguration(BaseModel):
    class Config:
        extra = Extra.forbid

    metricConfiguration: Optional[List[MetricConfigurationDefinition]] = None
