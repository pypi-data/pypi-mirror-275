# generated by datamodel-codegen:
#   filename:  analytics/webAnalyticEventData.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional, Union

from pydantic import BaseModel, Extra, Field

from ..type import basic
from . import basic as basic_1
from .webAnalyticEventType import customEvent, pageViewEvent


class WebAnalyticEventData(BaseModel):
    class Config:
        extra = Extra.forbid

    eventId: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of the report.'
    )
    timestamp: Optional[basic.Timestamp] = Field(None, description='event timestamp')
    eventType: basic_1.WebAnalyticEventType = Field(..., description='event type')
    eventData: Optional[
        Union[pageViewEvent.PageViewData, customEvent.CustomData]
    ] = Field(None, description='Web analytic data captured')
