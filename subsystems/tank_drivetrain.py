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
    BASIC = 1
    PID = 2
    MPC = 3


class TankDrivetrain(object):
    left_motors = []
    left_master: SpeedControllerGroup
    right_motors = []
    right_master: SpeedControllerGroup

    SYSTEM: int

    def __init__(self, left_motors: list, right_motors: list, control_system: int = ControlSystem.BUILTIN):
        self.SYSTEM = control_system

        self.left_motors = left_motors
        self.right_motors = right_motors

        # Set control mode
        if self.SYSTEM == ControlSystem.BUILTIN:
            self.left_master = SpeedControllerGroup(*self.left_motors)
            self.right_master = SpeedControllerGroup(*self.right_motors)

            self.drivetrain = wpilib.drive.DifferentialDrive(self.left_master, self.right_master)

            self.drivetrain.setSafetyEnabled(True)
            self.drivetrain.tankDrive(0.0, 0.0)
            self.drivetrain.setExpiration(0.5)

        else:
            for motor in [*self.left_motors, *self.right_motors]:
                motor.set(motor.ControlMode.PercentOutput, 0.0)

        # TODO add self-diagnostics

    def set(self, left=0.0, right=0.0):
        if self.SYSTEM == ControlSystem.BUILTIN:
            self.drivetrain.tankDrive(leftSpeed=left, rightSpeed=right)

        elif self.SYSTEM == ControlSystem.BASIC:
            for motor in self.left_motors:
                motor.set(motor.ControlMode.PercentOutput, left)

            for motor in self.right_motors:
                motor.set(motor.ControlMode.PercentOutput, right)

    def stop(self):
        if self.SYSTEM == ControlSystem.BUILTIN:
            self.drivetrain.tankDrive(0.0, 0.0)
        elif self.SYSTEM == ControlSystem.BASIC:
            for motor in [*self.left_motors, *self.right_motors]:
                motor.set(motor.ControlMode.PercentOutput, 0.0)

