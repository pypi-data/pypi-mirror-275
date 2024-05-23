# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/bigQueryConnection.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from .....security.credentials import gcpCredentials
from .. import connectionBasicType


class BigqueryType(Enum):
    BigQuery = 'BigQuery'


class BigqueryScheme(Enum):
    bigquery = 'bigquery'


class BigQueryConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[BigqueryType] = Field(
        BigqueryType.BigQuery, description='Service Type', title='Service Type'
    )
    scheme: Optional[BigqueryScheme] = Field(
        BigqueryScheme.bigquery,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    hostPort: Optional[str] = Field(
        'bigquery.googleapis.com',
        description='BigQuery APIs URL.',
        title='Host and Port',
    )
    credentials: gcpCredentials.GCPCredentials = Field(
        ..., description='GCP Credentials', title='GCP Credentials'
    )
    taxonomyProjectID: Optional[List[str]] = Field(
        None,
        description='Project IDs used to fetch policy tags',
        title='Taxonomy Project IDs',
    )
    taxonomyLocation: Optional[str] = Field(
        'us',
        description='Taxonomy location used to fetch policy tags',
        title='Taxonomy Location',
    )
    usageLocation: Optional[str] = Field(
        'us',
        description='Location used to query INFORMATION_SCHEMA.JOBS_BY_PROJECT to fetch usage data. You can pass multi-regions, such as `us` or `eu`, or you specific region. Australia and Asia multi-regions are not yet in GA.',
        title='Usage Location',
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
    supportsDatabase: Optional[connectionBasicType.SupportsDatabase] = Field(
        None, title='Supports Database'
    )
    supportsQueryComment: Optional[connectionBasicType.SupportsQueryComment] = Field(
        None, title='Supports Query Comment'
    )
    sampleDataStorageConfig: Optional[
        connectionBasicType.SampleDataStorageConfig
    ] = Field(None, title='Storage Config for Sample Data')
