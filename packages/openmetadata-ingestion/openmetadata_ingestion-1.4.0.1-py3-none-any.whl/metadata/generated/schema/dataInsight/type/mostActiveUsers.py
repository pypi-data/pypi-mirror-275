# generated by datamodel-codegen:
#   filename:  dataInsight/type/mostActiveUsers.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic


class MostActiveUsers(BaseModel):
    class Config:
        extra = Extra.forbid

    userName: Optional[str] = Field(None, description='Name of a user')
    team: Optional[str] = Field(None, description='Team a user belongs to')
    lastSession: Optional[basic.Timestamp] = Field(
        None, description='date time of the most recent session for the user'
    )
    sessions: Optional[float] = Field(None, description='Total number of sessions')
    sessionDuration: Optional[float] = Field(
        None, description='Total duration of all sessions in seconds'
    )
    avgSessionDuration: Optional[float] = Field(
        None, description='avg. duration of a sessions in seconds'
    )
    pageViews: Optional[float] = Field(
        None, description='Total number of pages viewed by the user'
    )
