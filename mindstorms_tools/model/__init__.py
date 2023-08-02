from dataclasses import dataclass
from enum import Enum


class SensorTypes(Enum):
    DISCONNECTED = 0
    SIMPLE_MEDIUM_LINEAR_MOTOR = 1
    TRAIN_MOTOR = 2
    LIGHT = 8
    COLOR_AND_DISTANCE = 37
    MEDIUM_LINEAR_MOTOR = 38
    TECHNIC_LARGE_MOTOR = 46
    TECHNIC_XL_MOTOR = 47
    COLOR_SENSOR = 61
    ULTRASONIC_DISTANCE = 62
    FORCE_SENSOR = 63
    COLOR_LIGHT_MATRIX = 64
    MEDIUM_ANGULAR_MOTOR = 75
    LARGE_ANGULAR_MOTOR = 76


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
