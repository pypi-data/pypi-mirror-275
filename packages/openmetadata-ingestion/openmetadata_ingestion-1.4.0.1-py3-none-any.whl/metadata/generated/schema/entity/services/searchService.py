# generated by datamodel-codegen:
#   filename:  entity/services/searchService.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference, entityReferenceList, tagLabel
from .connections import testConnectionResult
from .connections.search import (
    customSearchConnection,
    elasticSearchConnection,
    openSearchConnection,
)


class SearchServiceType(Enum):
    ElasticSearch = 'ElasticSearch'
    OpenSearch = 'OpenSearch'
    CustomSearch = 'CustomSearch'


class SearchConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    config: Optional[
        Union[
            elasticSearchConnection.ElasticsearchConnection,
            openSearchConnection.OpensearchConnection,
            customSearchConnection.CustomSearchConnection,
        ]
    ] = None


class SearchService(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier of this search service instance.'
    )
    name: basic.EntityName = Field(
        ..., description='Name that identifies this search service.'
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this search service.'
    )
    serviceType: SearchServiceType = Field(
        ..., description='Type of search service such as S3, GCS, AZURE...'
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of a search service instance.'
    )
    connection: Optional[SearchConnection] = None
    pipelines: Optional[entityReferenceList.EntityReferenceList] = Field(
        None,
        description='References to pipelines deployed for this search service to extract metadata etc..',
    )
    testConnectionResult: Optional[testConnectionResult.TestConnectionResult] = Field(
        None, description='Last test connection results for this service'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this search Service.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this search service.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this search service.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
    dataProducts: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='List of data products this entity is part of.'
    )
    domain: Optional[entityReference.EntityReference] = Field(
        None, description='Domain the search service belongs to.'
    )
