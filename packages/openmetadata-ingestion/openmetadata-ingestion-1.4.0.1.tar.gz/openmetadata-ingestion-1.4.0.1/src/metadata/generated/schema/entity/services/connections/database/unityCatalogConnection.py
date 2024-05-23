# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/unityCatalogConnection.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class DatabricksType(Enum):
    UnityCatalog = 'UnityCatalog'


class DatabricksScheme(Enum):
    databricks_connector = 'databricks+connector'


class UnityCatalogConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[DatabricksType] = Field(
        DatabricksType.UnityCatalog, description='Service Type', title='Service Type'
    )
    scheme: Optional[DatabricksScheme] = Field(
        DatabricksScheme.databricks_connector,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    hostPort: str = Field(
        ...,
        description='Host and port of the Databricks service.',
        title='Host and Port',
    )
    token: CustomSecretStr = Field(
        ..., description='Generated Token to connect to Databricks.', title='Token'
    )
    httpPath: Optional[str] = Field(
        None, description='Databricks compute resources URL.', title='Http Path'
    )
    catalog: Optional[str] = Field(
        None,
        description='Catalog of the data source(Example: hive_metastore). This is optional parameter, if you would like to restrict the metadata reading to a single catalog. When left blank, OpenMetadata Ingestion attempts to scan all the catalog.',
        title='Catalog',
    )
    databaseSchema: Optional[str] = Field(
        None,
        description='Database Schema of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single schema. When left blank, OpenMetadata Ingestion attempts to scan all the schemas.',
        title='Database Schema',
    )
    connectionTimeout: Optional[int] = Field(
        120,
        description='The maximum amount of time (in seconds) to wait for a successful connection to the data source. If the connection attempt takes longer than this timeout period, an error will be returned.',
        title='Connection Timeout',
    )
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = Field(
        None, title='Connection Options'
    )
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = Field(
        None, title='Connection Arguments'
    )
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = None
    supportsLineageExtraction: Optional[
        connectionBasicType.SupportsLineageExtraction
    ] = None
    supportsDBTExtraction: Optional[connectionBasicType.SupportsDBTExtraction] = None
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
    supportsDatabase: Optional[connectionBasicType.SupportsDatabase] = Field(
        None, title='Supports Database'
    )
    supportsQueryComment: Optional[connectionBasicType.SupportsQueryComment] = Field(
        None, title='Supports Query Comment'
    )
    sampleDataStorageConfig: Optional[
        connectionBasicType.SampleDataStorageConfig
    ] = Field(None, title='Storage Config for Sample Data')
