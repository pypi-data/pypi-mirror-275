# generated by datamodel-codegen:
#   filename:  analytics/reportDataType/webAnalyticUserActivityReportData.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic


class WebAnalyticUserActivityReportData(BaseModel):
    class Config:
        extra = Extra.forbid

    userName: Optional[str] = Field(None, description='user name')
    userId: Optional[basic.Uuid] = Field(None, description='user ID in OM')
    team: Optional[str] = Field(None, description='the team the user belongs to')
    totalSessions: Optional[int] = Field(None, description='total number of sessions')
    totalSessionDuration: Optional[int] = Field(None, description='total user count')
    totalPageView: Optional[int] = Field(None, description='total user count')
    lastSession: Optional[basic.Timestamp] = Field(None, description='latest session')
