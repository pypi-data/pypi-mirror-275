# generated by datamodel-codegen:
#   filename:  security/credentials/gcpExternalAccount.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, Field


class GcpExternalAccount(BaseModel):
    externalType: Optional[str] = Field(
        'external_account',
        description='Google Cloud Platform account type.',
        title='Credentials Type',
    )
    audience: Optional[str] = Field(
        None,
        description='Google Security Token Service audience which contains the resource name for the workload identity pool and the provider identifier in that pool.',
        title='Audience',
    )
    subjectTokenType: Optional[str] = Field(
        None,
        description='Google Security Token Service subject token type based on the OAuth 2.0 token exchange spec.',
        title='Subject Token Type',
    )
    tokenURL: Optional[str] = Field(
        None,
        description='Google Security Token Service token exchange endpoint.',
        title='Token URL',
    )
    credentialSource: Optional[Dict[str, str]] = Field(
        None,
        description='This object defines the mechanism used to retrieve the external credential from the local environment so that it can be exchanged for a GCP access token via the STS endpoint',
        title='Credential Source',
    )
