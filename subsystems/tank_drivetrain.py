import logging

import wpilib
from ctre import WPI_TalonSRX
import wpilib.drive
from wpilib import SpeedControllerGroup
from wpilib.interfaces.speedcontroller import SpeedController
from wpilib import Talon

logging.basicConfig(level=logging.DEBUG)

# TODO ADD MPC AND PID YOU LITERALLY NEED IT FOR THIS TO WORK


class ControlSystem:
    BUILTIN = 0
    BASIC = 0


class ControlMode:
    STOP = -1
    IDLE = 0
    GO = 1


class TankDrivetrain(object):
    left_motors = []
    left_master: SpeedControllerGroup
    right_motors = []
    right_master: SpeedControllerGroup

    SYSTEM: int
    MODE: int

    def __init__(self, left_motors: list, right_motors: list, control_system: int = ControlSystem.BUILTIN):
        self.SYSTEM = control_system

        self.left_motors = left_motors
        self.right_motors = right_motors

        self.left_master = SpeedControllerGroup(*self.left_motors)
        self.right_master = SpeedControllerGroup(*self.right_motors)

        # Set control mode
        if self.SYSTEM == ControlSystem.BUILTIN:
            self.drivetrain = wpilib.drive.DifferentialDrive(self.left_master, self.right_master)

            self.drivetrain.setSafetyEnabled(True)
            self.drivetrain.tankDrive(0.0, 0.0)
            self.drivetrain.setExpiration(0.5)

        # TODO add self-diagnostics

        self.MODE = ControlMode.IDLE

    def set(self, left, right):
        if self.SYSTEM == ControlSystem.BUILTIN:
            if self.MODE == ControlMode.STOP:
                self.stop()
            else:
                self.drivetrain.tankDrive(leftSpeed=left, rightSpeed=right)
                self.MODE = ControlMode.GO

    def stop(self):
        if self.SYSTEM == ControlSystem.BUILTIN:
            self.drivetrain.tankDrive(0.0, 0.0)
        if self.MODE != ControlMode.STOP:
            self.MODE = ControlMode.STOP

