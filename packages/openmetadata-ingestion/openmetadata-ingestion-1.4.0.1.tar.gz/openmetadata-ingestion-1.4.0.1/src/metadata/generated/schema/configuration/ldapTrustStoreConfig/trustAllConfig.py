# generated by datamodel-codegen:
#   filename:  configuration/ldapTrustStoreConfig/trustAllConfig.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class TrustAllConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    examineValidityDates: Optional[bool] = Field(
        False, description='Examine validity dates of certificate'
    )
