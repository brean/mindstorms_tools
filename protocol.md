# LEGO Mindstorms communication protocol
The data can be read using a USB-cable on a LINUX PC.

The LEGO Mindstorms hub should identify as device at `/dev/ttyACM0` with 115200 baud.
A connection can be established using 

## Protocol description
The LEGO Mindstorms hub sends and receives data in JSON binary that can be encoded as simple string.

Some data inside this like python error messages is encoded as base64.

### BNF
MESSAGE <- { "m": int, ...}

---

MESSAGE <- { "m": 0, "p": PAYLOAD}

PAYLOAD <- [ SENSORS, RPY ...]

SENSORS <- [ SENSOR ] * 6

SENSOR <- [ SENSOR_TYPE, VALUES ]

VALUES <- [int]

RPY <- [int, int, int] # roll, pitch and yaw

### General description
```
{
  "m": int # integer type of messages
  ...
}
```

log messages:
```
{
  "m": 0,
  "p": [ # p equals payload
    # the first 6 values is sensor data from the ports on the hub, see sensors
    # the next 2 are 
    # X unknown
  ]
}
```

sensors:
```
[int, [int | None]]
```
The first value in sensors is the sensor type, if nothing is connected it is 0,
other sensors are:

- 1: simple medium linear motor
- 2: train motor
- 8: light
- 37: color and distance sensor
- 38: medium linear motor
- 46: Technic large motor
- 47: Technic XL motor
- 61: color sensor
- 62: ultrasonic distance sensor,
- 63: force sensor
- 64: 3x3 color light matrix
- 75: medium angular motor
- 76: large angular motor

