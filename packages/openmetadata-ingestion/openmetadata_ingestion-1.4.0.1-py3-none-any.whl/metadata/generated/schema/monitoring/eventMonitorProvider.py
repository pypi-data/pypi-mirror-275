# generated by datamodel-codegen:
#   filename:  monitoring/eventMonitorProvider.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from enum import Enum


class EventMonitorProvider(Enum):
    cloudwatch = 'cloudwatch'
    prometheus = 'prometheus'
