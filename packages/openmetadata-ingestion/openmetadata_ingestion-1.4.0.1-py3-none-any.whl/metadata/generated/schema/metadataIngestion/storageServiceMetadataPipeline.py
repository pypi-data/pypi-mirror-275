# generated by datamodel-codegen:
#   filename:  metadataIngestion/storageServiceMetadataPipeline.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Extra, Field

from ..type import filterPattern
from .storage import (
    storageMetadataADLSConfig,
    storageMetadataGCSConfig,
    storageMetadataHttpConfig,
    storageMetadataLocalConfig,
    storageMetadataS3Config,
)


class StorageMetadataConfigType(Enum):
    StorageMetadata = 'StorageMetadata'


class NoMetadataConfigurationSource(BaseModel):
    pass

    class Config:
        extra = Extra.forbid


class StorageServiceMetadataPipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[StorageMetadataConfigType] = Field(
        StorageMetadataConfigType.StorageMetadata, description='Pipeline type'
    )
    containerFilterPattern: Optional[filterPattern.FilterPattern] = Field(
        None, description='Regex to only fetch containers that matches the pattern.'
    )
    storageMetadataConfigSource: Optional[
        Union[
            NoMetadataConfigurationSource,
            storageMetadataLocalConfig.StorageMetadataLocalConfig,
            storageMetadataHttpConfig.StorageMetadataHttpConfig,
            storageMetadataS3Config.StorageMetadataS3Config,
            storageMetadataADLSConfig.StorageMetadataAdlsConfig,
            storageMetadataGCSConfig.StorageMetadataGcsConfig,
        ]
    ] = Field(None, title='Storage Metadata Configuration Source')
    markDeletedContainers: Optional[bool] = Field(
        True,
        description='Optional configuration to soft delete containers in OpenMetadata if the source containers are deleted. Also, if the topic is deleted, all the associated entities with that containers will be deleted',
        title='Mark Deleted Containers',
    )
