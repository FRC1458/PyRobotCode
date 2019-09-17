import logging

import wpilib
import wpilib.drive
from wpilib import SpeedControllerGroup, Timer
from wpilib.interfaces.speedcontroller import SpeedController
from ctre import TalonSRX, NeutralMode

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

    CONTROL_SYSTEM: int

    def __init__(self, timer: Timer, left_motors: list, right_motors: list, control_system: int = ControlSystem.BASIC,
                 invert_left: bool = True, invert_right: bool = False):
        self.CONTROL_SYSTEM = control_system

        self.timer = timer

        self.left_motors = left_motors
        self.right_motors = right_motors

        # Set control mode
        if self.CONTROL_SYSTEM == ControlSystem.BUILTIN:
            self.left_master = SpeedControllerGroup(*self.left_motors)
            self.right_master = SpeedControllerGroup(*self.right_motors)

            self.drivetrain = wpilib.drive.DifferentialDrive(self.left_master, self.right_master)

            self.drivetrain.setSafetyEnabled(True)
            self.drivetrain.tankDrive(0.0, 0.0)
            self.drivetrain.setExpiration(0.5)

        else:
            for motor in self.left_motors:
                motor: TalonSRX
                motor.setNeutralMode(NeutralMode.Brake)
                motor.set(motor.ControlMode.PercentOutput, 0.0)
                motor.setInverted(invert_left)

            for motor in self.right_motors:
                motor: TalonSRX
                motor.setNeutralMode(NeutralMode.Brake)
                motor.set(motor.ControlMode.PercentOutput, 0.0)
                motor.setInverted(invert_right)

    def set(self, left, right):
        if self.CONTROL_SYSTEM == ControlSystem.BUILTIN:
            self.drivetrain.tankDrive(leftSpeed=left, rightSpeed=right)

        elif self.CONTROL_SYSTEM == ControlSystem.BASIC:
            for motor in self.left_motors:
                motor.set(motor.ControlMode.PercentOutput, left)

            for motor in self.right_motors:
                motor.set(motor.ControlMode.PercentOutput, right)

    def stop(self):
        if self.CONTROL_SYSTEM == ControlSystem.BUILTIN:
            self.drivetrain.tankDrive(0.0, 0.0)
        elif self.CONTROL_SYSTEM == ControlSystem.BASIC:
            for motor in [*self.left_motors, *self.right_motors]:
                motor.set(motor.ControlMode.PercentOutput, 0.0)

    def test_all_motors(self, motor_percent=0.5, motor_run_time=5.0, cooldown_time=2.5):
        # TODO add/finish self-diagnostics
        if self.CONTROL_SYSTEM == ControlSystem.BASIC:
            for motor in [*self.left_motors, *self.right_motors]:
                motor: TalonSRX

                motor.set(motor.ControlMode.PercentOutput, motor_percent)
                self.timer.delay(motor_run_time)
                motor.set(motor.ControlMode.PercentOutput, motor_percent)

                self.timer.delay(cooldown_time)




