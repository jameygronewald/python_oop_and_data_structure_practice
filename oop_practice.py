from enum import Enum

class SecurityDevice:
    def __init__(self, active):
        self.active = active

    def reset(self):
        self.active = True

class Sensor(SecurityDevice):
    def __init__(self, silent, distance):
        self.silent = silent
        self.distance = distance

class Position:
    def __init__(self, pan, tilt, zoom):
        self.pan = pan
        self.tilt = tilt
        self.zoom = zoom
    
    def __str__(self):
        return f"Pan: {str(self.pan)}, Tilt: {str(self.zoom)} Zoom: {str(self.tilt)}."

    def __eq__(self, other):
        return self.pan == other.pan and self.tilt == other.tilt and self.zoom == other.zoom

    __hash__ = None


class Camera(SecurityDevice):
    def __init__(self, serial_number, position, camera_type):
        self.serial_number = serial_number
        self.position = position
        self.camera_type = camera_type

    def __str__(self):
        return f"Serial number: {str(self.serial_number)}, Camera type: {str(self.camera_type)}." + self.position.__str__()

    def __eq__(self, other):
        return self.serial_number == other.serial_number and self.position == other.position and self.camera_type == other.camera_type   

    __hash__ = None

    class CameraType(Enum):
        ptz = 0
        eptz = 1
        stationary = 2
    
position_one = Position(4, 3, 5)
position_two = Position(1, 0, 10)

camera_one = Camera('1111', position_one, Camera.CameraType.ptz)
camera_two = Camera('2222', position_two, Camera.CameraType.eptz)
camera_three = Camera('3333', position_one, Camera.CameraType.stationary)
