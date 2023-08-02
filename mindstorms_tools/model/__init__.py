from dataclasses import dataclass


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
