# generated by datamodel-codegen:
#   filename:  auth/createPersonalToken.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field

from . import jwtAuth


class CreatePersonalToken(BaseModel):
    class Config:
        extra = Extra.forbid

    tokenName: str = Field(..., description='Name of the Personal Access Token')
    JWTTokenExpiry: jwtAuth.JWTTokenExpiry
