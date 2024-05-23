# generated by datamodel-codegen:
#   filename:  security/client/googleSSOClientConfig.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr


class GoogleSSOClientConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    secretKey: CustomSecretStr = Field(
        ..., description='Google SSO client secret key path or contents.'
    )
    audience: Optional[str] = Field(
        'https://www.googleapis.com/oauth2/v4/token',
        description='Google SSO audience URL',
    )
