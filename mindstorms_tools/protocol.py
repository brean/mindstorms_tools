from .model import Message, Payload, Sensor, SensorTypes


def parse_sensor(sensor_data: list) -> list[Sensor]:
    """
    Create Sensor instances from data.
    """
    sensors = []
    for sensor in sensor_data:
        sensors.append(Sensor(type=SensorTypes(sensor[0]), value=sensor[1]))
    return sensors


def parse_message(data: str) -> Message:
    if 'm' not in data:
        raise RuntimeError(f'unknown data received: {data}')
        return

    msg_type = data['m']
    if msg_type == 0:
        sensors = parse_sensor(data['p'][0:6])
        return Message(
            type=msg_type,
            payload=Payload(
                sensors=sensors))
    elif msg_type == 2:
        # {'m': 2, 'p': [7.206, 40, True]}
        print(data)
        pass
    elif msg_type == 4:
        # motor data?
        # {'m': 4, 'p': 0}
        print(data)
        pass
    else:
        raise RuntimeError(f'unknown data received: {data}')
