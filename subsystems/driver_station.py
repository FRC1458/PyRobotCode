import wpilib


class DriverStation(object):
    left_joystick: wpilib.Joystick
    right_joystick: wpilib.Joystick

    def __init__(self, left_stick, right_stick):
        self.left_joystick = left_stick
        self.right_joystick = right_stick
        # TODO Add button system and a log button maybe


