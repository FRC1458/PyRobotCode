import logging
import time

from wpilib import TimedRobot, XboxController, run, Compressor, DoubleSolenoid
from ctre import TalonSRX

from robot_map import *

logging.basicConfig(level=logging.DEBUG)


# All timed functions should run at ~50 hz
class BaseRobot(TimedRobot):
    robot: RobotMap
    driver_station: DriverStation

    def robotInit(self) -> None:
        self.robot = RobotMap()
        self.driver_station = self.robot.driver_station

        print("Robot Initialized!")

    def robotPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        print("Driver Has Control!")

    def teleopPeriodic(self) -> None:
        l, r = self.driver_station.get_control_arcade()
        self.robot.drivetrain.set(l, r)

        self.robot.beak.update()

    def disabledInit(self) -> None:
        self.robot.drivetrain.stop()

    def disabledPeriodic(self) -> None:
        pass

    def testInit(self) -> None:
        self.robot.drivetrain.stop()

    def testPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    run(BaseRobot)
