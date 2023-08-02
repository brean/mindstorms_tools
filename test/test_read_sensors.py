from mindstorms_tools.protocol import parse_message
from mindstorms_tools.model import Sensor, Payload, Message, SensorTypes


def test_parse_data():
    """
    test some data with multiple connected distance sensors
    """
    data = {
        "m": 0,
        "p": [[62, [None]], [62, [4]], [62, [10]], [0, []], [0, []], [0, []]]}
    result = parse_message(data)
    assert result == Message(
        type=0,
        payload=Payload(
            sensors=[
                Sensor(type=SensorTypes.ULTRASONIC_DISTANCE, value=[None]),
                Sensor(type=SensorTypes.ULTRASONIC_DISTANCE, value=[4]),
                Sensor(type=SensorTypes.ULTRASONIC_DISTANCE, value=[10]),
                Sensor(type=SensorTypes.DISCONNECTED, value=[]),
                Sensor(type=SensorTypes.DISCONNECTED, value=[]),
                Sensor(type=SensorTypes.DISCONNECTED, value=[])
            ]
        ))
