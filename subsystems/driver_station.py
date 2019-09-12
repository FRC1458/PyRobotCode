from wpilib import Joystick


class DriverStation(object):
    left_joystick: Joystick
    right_joystick: Joystick

    def __init__(self, left_stick, right_stick):
        self.left_joystick = left_stick
        self.right_joystick = right_stick
        # TODO Add button system and a log button maybe


