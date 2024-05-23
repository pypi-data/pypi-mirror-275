# generated by datamodel-codegen:
#   filename:  security/client/oktaSSOClientConfig.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr


class OktaSSOClientConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    clientId: str = Field(..., description='Okta Client ID.')
    orgURL: str = Field(..., description='Okta org url.')
    privateKey: CustomSecretStr = Field(..., description='Okta Private Key.')
    email: str = Field(..., description='Okta Service account Email.')
    scopes: Optional[List[str]] = Field(None, description='Okta client scopes.')
