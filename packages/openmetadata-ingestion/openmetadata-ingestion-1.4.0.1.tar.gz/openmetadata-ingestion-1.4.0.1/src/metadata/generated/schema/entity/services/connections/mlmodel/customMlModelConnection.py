# generated by datamodel-codegen:
#   filename:  entity/services/connections/mlmodel/customMlModelConnection.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from .. import connectionBasicType


class CustomMlModelType(Enum):
    CustomMlModel = 'CustomMlModel'


class CustomMlModelConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: CustomMlModelType = Field(
        ..., description='Custom Ml model service type', title='Service Type'
    )
    sourcePythonClass: Optional[str] = Field(
        None,
        description='Source Python Class Name to instantiated by the ingestion workflow',
        title='Source Python Class Name',
    )
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = Field(
        None, title='Connection Options'
    )
