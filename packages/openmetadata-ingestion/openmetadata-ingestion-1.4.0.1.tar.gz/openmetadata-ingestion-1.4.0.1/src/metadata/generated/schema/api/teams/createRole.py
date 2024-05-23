# generated by datamodel-codegen:
#   filename:  api/teams/createRole.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic


class CreateRoleRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName
    displayName: Optional[str] = Field(
        None,
        description="Optional name used for display purposes. Example 'Data Consumer'",
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Optional description of the role'
    )
    policies: List[basic.EntityName] = Field(
        ...,
        description='Policies that is attached to this role. At least one policy is required.',
    )
