from wpilib import Joystick, XboxController
from wpilib.interfaces import GenericHID


def constrain(n, low, high):
    return min(max(n, low), high)


class DriverStation(object):
    controller: XboxController or Joystick

    invert_turning: bool
    invert_acceleration: bool

    def __init__(self, controller, invert_turning=True, invert_acceleration=False):
        self.controller = controller

        self.invert_turning = invert_turning
        self.invert_acceleration = invert_acceleration

    def get_control_arcade(self, turn_limit=0.35, acceleration_limit=0.60):
        acceleration = self.controller.getY(hand=GenericHID.Hand.kLeft) * acceleration_limit
        turning = self.controller.getX(hand=GenericHID.Hand.kRight) * turn_limit

        if self.invert_turning:
            turning = turning * -1.0

        if self.invert_acceleration:
            acceleration = acceleration * -1.0

        return constrain(acceleration + turning, -1.0, 1.0), constrain(acceleration - turning, -1.0, 1.0)







