# generated by datamodel-codegen:
#   filename:  auth/changePasswordRequest.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field


class RequestType(Enum):
    SELF = 'SELF'
    USER = 'USER'


class ChangePasswordRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    username: Optional[str] = Field(None, description='Name of the user')
    oldPassword: Optional[str] = Field(
        None, description='Name that identifies this Custom Metric.'
    )
    newPassword: str = Field(..., description='Name of the column in a table.')
    confirmPassword: str = Field(..., description='Name of the column in a table.')
    requestType: Optional[RequestType] = Field(
        RequestType.SELF, description='Name of the column in a table.'
    )
