# using pyserial to forward python code to a Hub and execute it
# from mindstorms_tools.model import Message, Payload, Sensor
from mindstorms_tools.com import connect, HUB
from mindstorms_tools.model import Message


def handle_msg(msg: Message):
    print(msg)


def main():
    # connect to Hub
    connect(handle_msg=handle_msg, hub=HUB)


if __name__ == '__main__':
    main()
