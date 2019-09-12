import logging
import time

from wpilib import TimedRobot, Joystick, run

from subsystems.driver_station import DriverStation
from robot_map import *

logging.basicConfig(level=logging.DEBUG)


# All timed functions should run at ~50 hz
class BaseRobot(TimedRobot):
    robot: RobotMap
    driver_station: DriverStation

    # TODO ADD ODOMETRY SUBSYSTEM
    def robotInit(self) -> None:
        self.robot = RobotMap()
        self.driver_station = DriverStation(Joystick(0), Joystick(1))

        # self.joy = wpilib.Joystick(0)
        # self.motor1 = TalonSRX(10)
        # self.motor2 = TalonSRX(31)

        print("Robot Initialized!")

    def robotPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        print("Driver Has Control!")

    def teleopPeriodic(self) -> None:
        self.robot.drivetrain.set(self.ds.left_joystick.getY() * 1.0, self.ds.right_joystick.getY() * 1.0)

        # self.motor1.set(self.motor1.ControlMode.PercentOutput, 0.5)
        # self.motor2.set(self.motor1.ControlMode.PercentOutput, 0.5)

    def disabledInit(self) -> None:
        self.robot.drivetrain.stop()

        # self.motor1.set(self.motor1.ControlMode.PercentOutput, 0.0)
        # self.motor2.set(self.motor1.ControlMode.PercentOutput, 0.0)

    def disabledPeriodic(self) -> None:
        self.robot.drivetrain.stop()

        # print(self.joy.ds.getStickAxis(0, 0))


if __name__ == "__main__":
    run(BaseRobot)
