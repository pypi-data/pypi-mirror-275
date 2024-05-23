# generated by datamodel-codegen:
#   filename:  entity/services/connections/search/elasticSearch/apiAuth.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr


class ApiKeyAuthentication(BaseModel):
    class Config:
        extra = Extra.forbid

    apiKey: Optional[CustomSecretStr] = Field(
        None,
        description='Elastic Search API Key for API Authentication',
        title='API Key',
    )
    apiKeyId: Optional[str] = Field(
        None,
        description='Elastic Search API Key ID for API Authentication',
        title='API Key ID',
    )
