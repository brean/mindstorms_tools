from dataclasses import dataclass
from enum import Enum


class SensorTypes(Enum):
    DISCONNECTED: int = 0
    ULTRASONIC_DISTANCE: int = 62


@dataclass
class Sensor:
    type: int
    value: list[int] | None


@dataclass
class Payload:
    sensors: list[Sensor]


@dataclass
class Message:
    type: int
    payload: list[Payload]
