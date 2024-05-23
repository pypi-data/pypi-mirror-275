# generated by datamodel-codegen:
#   filename:  entity/teams/team.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference, entityReferenceList, profile


class TeamType(Enum):
    Group = 'Group'
    Department = 'Department'
    Division = 'Division'
    BusinessUnit = 'BusinessUnit'
    Organization = 'Organization'


class Team(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid
    teamType: Optional[TeamType] = Field(TeamType.Group, description='Team type')
    name: basic.EntityName = Field(
        ...,
        description='A unique name of the team typically the team ID from an identity provider. Example - group Id from LDAP.',
    )
    email: Optional[basic.Email] = Field(None, description='Email address of the team.')
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    displayName: Optional[str] = Field(
        None, description="Name used for display purposes. Example 'Data Science team'."
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the team.'
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
        None, description='Link to the resource corresponding to this entity.'
    )
    profile: Optional[profile.Profile] = Field(
        None, description='Team profile information.'
    )
    parents: Optional[entityReferenceList.EntityReferenceList] = Field(
        None,
        description='Parent teams. For an `Organization` the `parent` is always null. A `BusinessUnit` always has only one parent of type `BusinessUnit` or an `Organization`. A `Division` can have multiple parents of type `BusinessUnit` or `Division`. A `Department` can have multiple parents of type `Division` or `Department`.',
    )
    children: Optional[entityReferenceList.EntityReferenceList] = Field(
        None,
        description='Children teams. An `Organization` can have `BusinessUnit`, `Division` or `Department` as children. A `BusinessUnit` can have `BusinessUnit`, `Division`, or `Department` as children. A `Division` can have `Division` or `Department` as children. A `Department` can have `Department` as children.',
    )
    users: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='Users that are part of the team.'
    )
    childrenCount: Optional[int] = Field(
        None, description='Total count of Children teams.'
    )
    userCount: Optional[int] = Field(
        None, description='Total count of users that are part of the team.'
    )
    owns: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='List of entities owned by the team.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this team. '
    )
    isJoinable: Optional[bool] = Field(
        True,
        description='Can any user join this team during sign up? Value of true indicates yes, and false no.',
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
    defaultRoles: Optional[entityReferenceList.EntityReferenceList] = Field(
        None,
        description='Default roles of a team. These roles will be inherited by all the users that are part of this team.',
    )
    inheritedRoles: Optional[entityReferenceList.EntityReferenceList] = Field(
        None,
        description='Roles that a team is inheriting through membership in teams that have set team default roles.',
    )
    policies: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='Policies that is attached to this team.'
    )
    domain: Optional[entityReference.EntityReference] = Field(
        None, description='Domain the Team belongs to.'
    )
