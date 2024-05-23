# generated by datamodel-codegen:
#   filename:  api/feed/closeTask.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic


class CloseTaskRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    comment: str = Field(
        ..., description='The closing comment explaining why the task is being closed.'
    )
    testCaseFQN: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='Fully qualified name of the test case.'
    )
