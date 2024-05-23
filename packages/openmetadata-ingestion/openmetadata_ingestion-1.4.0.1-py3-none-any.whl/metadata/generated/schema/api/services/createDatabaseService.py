# generated by datamodel-codegen:
#   filename:  api/services/createDatabaseService.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.services import databaseService
from ...type import basic, entityReference, tagLabel


class CreateDatabaseServiceRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName = Field(
        ..., description='Name that identifies the this entity instance uniquely'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this database service.'
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of Database entity.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this Database Service.'
    )
    serviceType: databaseService.DatabaseServiceType
    connection: Optional[databaseService.DatabaseConnection] = None
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this database service.'
    )
    dataProducts: Optional[List[basic.FullyQualifiedEntityName]] = Field(
        None,
        description='List of fully qualified names of data products this entity is part of.',
    )
    domain: Optional[str] = Field(
        None,
        description='Fully qualified name of the domain the Database Service belongs to.',
    )
