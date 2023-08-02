# using pyserial to forward python code to a Hub and execute it
import json
import serial
from .protocol import parse_message


HUB = '/dev/ttyACM0'


def connect(handle_msg, hub: str = HUB):
    # connect to Hub
    ser = serial.Serial(port=hub, baudrate=115200)
    if not ser.isOpen():
        print('Can not connect to HUB')
        return

    while True:
        try:
            data = json.loads(ser.read_until(b'\r'))
        except json.JSONDecodeError as e:
            print(e)
            continue
        handle_msg(parse_message(data))
