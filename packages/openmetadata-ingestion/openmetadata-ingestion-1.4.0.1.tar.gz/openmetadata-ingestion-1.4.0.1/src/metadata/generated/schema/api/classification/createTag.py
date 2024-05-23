# generated by datamodel-codegen:
#   filename:  api/classification/createTag.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic


class CreateTagRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    classification: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='Name of the classification that this tag is part of.'
    )
    parent: Optional[basic.FullyQualifiedEntityName] = Field(
        None,
        description='Fully qualified name of the parent tag. When null, the term is at the root of the classification.',
    )
    name: basic.EntityName
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this tag.'
    )
    description: basic.Markdown = Field(
        ..., description='Unique name of the classification'
    )
    style: Optional[basic.Style] = None
    associatedTags: Optional[List[str]] = Field(
        None, description='Fully qualified names of tags associated with this tag'
    )
    provider: Optional[basic.ProviderType] = basic.ProviderType.user
    mutuallyExclusive: Optional[bool] = Field(
        'false',
        description='Children tags under this group are mutually exclusive. When mutually exclusive is `true` the tags from this group are used to **classify** an entity. An entity can only be in one class - example, it can only be either `tier1` or `tier2` and not both. When mutually exclusive is `false`, the tags from this group are used to **categorize** an entity. An entity can be in multiple categories simultaneously - example a customer can be `newCustomer` and `atRisk` simultaneously.',
    )
