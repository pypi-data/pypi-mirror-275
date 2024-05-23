# generated by datamodel-codegen:
#   filename:  configuration/fernetConfiguration.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class FernetConfiguration(BaseModel):
    class Config:
        extra = Extra.forbid

    fernetKey: str = Field(..., description='Fernet Key')
