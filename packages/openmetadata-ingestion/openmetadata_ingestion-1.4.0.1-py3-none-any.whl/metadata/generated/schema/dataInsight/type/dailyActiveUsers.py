# generated by datamodel-codegen:
#   filename:  dataInsight/type/dailyActiveUsers.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic


class DailyActiveUsers(BaseModel):
    class Config:
        extra = Extra.forbid

    timestamp: Optional[basic.Timestamp] = Field(None, description='timestamp')
    activeUsers: Optional[int] = Field(
        None, description='Number of active users (user with at least 1 session).'
    )
