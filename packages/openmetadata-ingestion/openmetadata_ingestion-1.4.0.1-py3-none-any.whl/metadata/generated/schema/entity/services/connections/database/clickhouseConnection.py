# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/clickhouseConnection.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class ClickhouseType(Enum):
    Clickhouse = 'Clickhouse'


class ClickhouseScheme(Enum):
    clickhouse_http = 'clickhouse+http'
    clickhouse_native = 'clickhouse+native'


class ClickhouseConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[ClickhouseType] = Field(
        ClickhouseType.Clickhouse, description='Service Type', title='Service Type'
    )
    scheme: Optional[ClickhouseScheme] = Field(
        ClickhouseScheme.clickhouse_http,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: Optional[str] = Field(
        None,
        description='Username to connect to Clickhouse. This user should have privileges to read all the metadata in Clickhouse.',
        title='Username',
    )
    password: Optional[CustomSecretStr] = Field(
        None, description='Password to connect to Clickhouse.', title='Password'
    )
    hostPort: str = Field(
        ...,
        description='Host and port of the Clickhouse service.',
        title='Host and Port',
    )
    databaseName: Optional[str] = Field(
        None,
        description='Optional name to give to the database in OpenMetadata. If left blank, we will use default as the database name.',
        title='Database Name',
    )
    databaseSchema: Optional[str] = Field(
        None,
        description='Database Schema of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single schema. When left blank, OpenMetadata Ingestion attempts to scan all the schemas.',
        title='Database Schema',
    )
    duration: Optional[int] = Field(
        None, description='Clickhouse SQL connection duration.', title='Duration'
    )
    https: Optional[bool] = Field(
        None,
        description='Use HTTPS Protocol for connection with clickhouse',
        title='Use HTTPS Protocol',
    )
    secure: Optional[bool] = Field(
        None,
        description='Establish secure connection with clickhouse',
        title='Secure Connection',
    )
    keyfile: Optional[str] = Field(
        None,
        description='Path to key file for establishing secure connection',
        title='Key File Path',
    )
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = Field(
        None, title='Connection Options'
    )
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = Field(
        None, title='Connection Arguments'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = None
    supportsLineageExtraction: Optional[
        connectionBasicType.SupportsLineageExtraction
    ] = None
    supportsDBTExtraction: Optional[connectionBasicType.SupportsDBTExtraction] = None
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
    supportsQueryComment: Optional[connectionBasicType.SupportsQueryComment] = Field(
        None, title='Supports Query Comment'
    )
    sampleDataStorageConfig: Optional[
        connectionBasicType.SampleDataStorageConfig
    ] = Field(None, title='Storage Config for Sample Data')
