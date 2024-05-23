# generated by datamodel-codegen:
#   filename:  entity/services/connections/search/elasticSearchConnection.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, Extra, Field

from .. import connectionBasicType
from ..common import sslConfig
from .elasticSearch import apiAuth, basicAuth


class ElasticSearchType(Enum):
    ElasticSearch = 'ElasticSearch'


class ElasticsearchConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[ElasticSearchType] = Field(
        ElasticSearchType.ElasticSearch,
        description='ElasticSearch Type',
        title='ElasticSearch Type',
    )
    hostPort: Optional[AnyUrl] = Field(
        None,
        description='Host and port of the ElasticSearch service.',
        title='Host and Port',
    )
    authType: Optional[
        Union[basicAuth.BasicAuthentication, apiAuth.ApiKeyAuthentication]
    ] = Field(
        None, description='Choose Auth Config Type.', title='Auth Configuration Type'
    )
    sslConfig: Optional[sslConfig.SslConfig] = Field(None, title='SSL Config')
    connectionTimeoutSecs: Optional[int] = Field(
        30,
        description='Connection Timeout in Seconds',
        title='Connection Timeout in Seconds',
    )
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = Field(
        None, title='Connection Arguments'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
