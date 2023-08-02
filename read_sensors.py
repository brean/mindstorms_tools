# using pyserial to forward python code to a Hub and execute it
# from mindstorms_tools.model import Message, Payload, Sensor
from mindstorms_tools.com import connect


HUB = '/dev/ttyACM0'


def main():
    # connect to Hub
    connect(port=HUB)


if __name__ == '__main__':
    main()
