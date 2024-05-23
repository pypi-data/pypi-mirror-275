# generated by datamodel-codegen:
#   filename:  entity/services/connections/pipeline/backendConnection.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field


class BackendType(Enum):
    Backend = 'Backend'


class BackendConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[BackendType] = Field(
        BackendType.Backend, description='Service Type', title='Service Type'
    )
