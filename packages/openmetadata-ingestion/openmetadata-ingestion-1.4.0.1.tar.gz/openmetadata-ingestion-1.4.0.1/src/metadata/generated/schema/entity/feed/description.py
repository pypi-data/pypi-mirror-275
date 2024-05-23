# generated by datamodel-codegen:
#   filename:  entity/feed/description.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class DescriptionFeedInfo(BaseModel):
    class Config:
        extra = Extra.forbid

    previousDescription: Optional[str] = Field(
        None, description='The previous description of the entity.'
    )
    newDescription: Optional[str] = Field(
        None, description='The new description of the entity.'
    )
    diffMessage: Optional[str] = Field(
        None, description='The difference between the previous and new descriptions.'
    )
