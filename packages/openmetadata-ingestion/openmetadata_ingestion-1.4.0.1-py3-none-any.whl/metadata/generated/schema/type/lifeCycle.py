# generated by datamodel-codegen:
#   filename:  type/lifeCycle.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from . import basic, entityReference


class AccessDetails(BaseModel):
    class Config:
        extra = Extra.forbid

    timestamp: basic.Timestamp = Field(
        ..., description='Timestamp of data asset accessed for creation, update, read.'
    )
    accessedBy: Optional[entityReference.EntityReference] = Field(
        None,
        description='User, Pipeline, Query that created,updated or accessed the data asset',
    )
    accessedByAProcess: Optional[str] = Field(
        None,
        description='Any process that accessed the data asset that is not captured in OpenMetadata.',
    )


class LifeCycle(BaseModel):
    class Config:
        extra = Extra.forbid

    created: Optional[AccessDetails] = Field(
        None, description='Access Details about created aspect of the data asset'
    )
    updated: Optional[AccessDetails] = Field(
        None, description='Access Details about updated aspect of the data asset'
    )
    accessed: Optional[AccessDetails] = Field(
        None, description='Access Details about accessed aspect of the data asset'
    )
