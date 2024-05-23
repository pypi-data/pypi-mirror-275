# generated by datamodel-codegen:
#   filename:  api/data/createGlossaryTerm.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.data import glossaryTerm
from ...type import basic, entityReference, tagLabel


class CreateGlossaryTermRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    glossary: basic.FullyQualifiedEntityName = Field(
        ..., description='FullyQualifiedName of the glossary that this term is part of.'
    )
    parent: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='Fully qualified name of  the parent glossary term.'
    )
    name: basic.EntityName = Field(
        ..., description='Preferred name for the glossary term.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this glossary term.'
    )
    description: basic.Markdown = Field(
        ..., description='Description of the glossary term.'
    )
    style: Optional[basic.Style] = None
    synonyms: Optional[List[basic.EntityName]] = Field(
        None,
        description='Alternate names that are synonyms or near-synonyms for the glossary term.',
    )
    relatedTerms: Optional[List[basic.FullyQualifiedEntityName]] = Field(
        None,
        description='Other array of glossary term fully qualified names that are related to this glossary term.',
    )
    references: Optional[List[glossaryTerm.TermReference]] = Field(
        None, description='Link to a reference from an external glossary.'
    )
    reviewers: Optional[List[basic.EntityName]] = Field(
        None, description='User names of the reviewers for this glossary.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this glossary term.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this glossary term.'
    )
    provider: Optional[basic.ProviderType] = basic.ProviderType.user
    mutuallyExclusive: Optional[bool] = Field(
        'false',
        description='Glossary terms that are children of this term are mutually exclusive. When mutually exclusive is `true` only one term can be used to label an entity from this group. When mutually exclusive is `false`, multiple terms from this group can be used to label an entity.',
    )
    extension: Optional[basic.EntityExtension] = Field(
        None,
        description='Entity extension data with custom attributes added to the entity.',
    )
