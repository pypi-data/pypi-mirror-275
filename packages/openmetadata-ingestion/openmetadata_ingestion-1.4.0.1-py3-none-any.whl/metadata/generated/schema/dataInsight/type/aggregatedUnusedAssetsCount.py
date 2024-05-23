# generated by datamodel-codegen:
#   filename:  dataInsight/type/aggregatedUnusedAssetsCount.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...analytics.reportDataType import aggregatedCostAnalysisReportData
from ...type import basic


class AggregatedUnusedAssetsCount(BaseModel):
    class Config:
        extra = Extra.forbid

    timestamp: Optional[basic.Timestamp] = Field(None, description='timestamp')
    frequentlyUsedDataAssets: Optional[
        aggregatedCostAnalysisReportData.DataAssetValues
    ] = Field(None, description='Frequently used Data Assets')
    unusedDataAssets: Optional[
        aggregatedCostAnalysisReportData.DataAssetValues
    ] = Field(None, description='Unused Data Assets')
