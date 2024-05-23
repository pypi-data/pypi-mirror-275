# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/sasConnection.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Optional, Union

from pydantic import AnyUrl, BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr


class SasType(Enum):
    SAS = 'SAS'


class SASConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[SasType] = Field(SasType.SAS, description='Service Type')
    username: str = Field(..., description='Username to connect to SAS Viya.')
    password: CustomSecretStr = Field(
        ..., description='Password to connect to SAS Viya'
    )
    serverHost: AnyUrl = Field(..., description='Hostname of SAS Viya deployment.')
    datatables: Optional[bool] = Field(
        True, description='Enable datatables for ingestion'
    )
    dataTablesCustomFilter: Optional[Union[Dict[str, Any], str]] = Field(
        None,
        description='Custom filter for datatables',
        title='Custom Filter for datatables',
    )
    reports: Optional[bool] = Field(False, description='Enable report for ingestion')
    reportsCustomFilter: Optional[Union[Dict[str, Any], str]] = Field(
        None, description='Custom filter for reports', title='Custom Filter for reports'
    )
    dataflows: Optional[bool] = Field(
        False, description='Enable dataflow for ingestion'
    )
    dataflowsCustomFilter: Optional[Union[Dict[str, Any], str]] = Field(
        None,
        description='Custom filter for dataflows',
        title='Custom Filter for dataflows',
    )
