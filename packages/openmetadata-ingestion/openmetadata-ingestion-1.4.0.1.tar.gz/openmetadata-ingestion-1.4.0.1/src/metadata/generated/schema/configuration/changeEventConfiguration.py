# generated by datamodel-codegen:
#   filename:  configuration/changeEventConfiguration.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra


class ChangeEventConfiguration(BaseModel):
    class Config:
        extra = Extra.forbid

    omUri: Optional[str] = None
