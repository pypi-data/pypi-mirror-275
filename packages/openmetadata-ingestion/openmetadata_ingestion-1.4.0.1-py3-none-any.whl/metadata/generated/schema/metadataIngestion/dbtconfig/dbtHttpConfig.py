# generated by datamodel-codegen:
#   filename:  metadataIngestion/dbtconfig/dbtHttpConfig.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field


class DbtConfigType(Enum):
    http = 'http'


class DbtHttpConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    dbtConfigType: DbtConfigType = Field(..., description='dbt Configuration type')
    dbtCatalogHttpPath: Optional[str] = Field(
        None,
        description='DBT catalog http file path to extract dbt models with their column schemas.',
        title='DBT Catalog HTTP File Path',
    )
    dbtManifestHttpPath: str = Field(
        ...,
        description='DBT manifest http file path to extract dbt models and associate with tables.',
        title='DBT Manifest HTTP File Path',
    )
    dbtRunResultsHttpPath: Optional[str] = Field(
        None,
        description='DBT run results http file path to extract the test results information.',
        title='DBT Run Results HTTP File Path',
    )
