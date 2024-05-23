# generated by datamodel-codegen:
#   filename:  type/entityReference.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from . import basic


class EntityReference(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies an entity instance.'
    )
    type: str = Field(
        ...,
        description='Entity type/class name - Examples: `database`, `table`, `metrics`, `databaseService`, `dashboardService`...',
    )
    name: Optional[str] = Field(None, description='Name of the entity instance.')
    fullyQualifiedName: Optional[str] = Field(
        None,
        description="Fully qualified name of the entity instance. For entities such as tables, databases fullyQualifiedName is returned in this field. For entities that don't have name hierarchy such as `user` and `team` this will be same as the `name` field.",
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Optional description of entity.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this entity.'
    )
    deleted: Optional[bool] = Field(
        None, description='If true the entity referred to has been soft-deleted.'
    )
    inherited: Optional[bool] = Field(
        None,
        description='If true the relationship indicated by this entity reference is inherited from the parent entity.',
    )
    href: Optional[basic.Href] = Field(None, description='Link to the entity resource.')
