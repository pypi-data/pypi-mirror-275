# generated by datamodel-codegen:
#   filename:  configuration/dataQualityConfiguration.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class DataQualityConfiguration(BaseModel):
    class Config:
        extra = Extra.forbid

    severityIncidentClassifier: str = Field(
        ..., description='Class Name for the severity incident classifier.'
    )
