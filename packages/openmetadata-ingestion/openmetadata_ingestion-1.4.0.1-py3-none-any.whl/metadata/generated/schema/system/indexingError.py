# generated by datamodel-codegen:
#   filename:  system/indexingError.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra

from . import entityError


class ErrorSource(Enum):
    Job = 'Job'
    Reader = 'Reader'
    Processor = 'Processor'
    Sink = 'Sink'


class IndexingAppError(BaseModel):
    class Config:
        extra = Extra.forbid

    errorSource: Optional[ErrorSource] = None
    lastFailedCursor: Optional[str] = None
    message: Optional[str] = None
    failedEntities: Optional[List[entityError.EntityError]] = None
    reason: Optional[str] = None
    stackTrace: Optional[str] = None
    submittedCount: Optional[int] = None
    successCount: Optional[int] = None
    failedCount: Optional[int] = None
