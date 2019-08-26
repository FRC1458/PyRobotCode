import logging
import time

from wpilib import TimedRobot
import wpilib
from ctre import WPI_TalonSRX

from subsystems.tank_drivetrain import TankDrivetrain
from subsystems.driver_station import DriverStation

logging.basicConfig(level=logging.DEBUG)


# All timed functions should run at 50 hz
class BaseRobot(TimedRobot):
    dt: TankDrivetrain
    ds: DriverStation
    timer: wpilib.Timer

    # TODO ADD ODOMETRY SUBSYSTEM
    def robotInit(self) -> None:
        self.dt = TankDrivetrain([wpilib.Talon(0)], [wpilib.Talon(1)])
        self.ds = DriverStation(wpilib.Joystick(0), wpilib.Joystick(1))
        self.timer = wpilib.Timer()

        print("Robot Initialized!")

    def robotPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        print("Driver Has Control!")

    def teleopPeriodic(self) -> None:
        self.dt.set(self.ds.left_joystick.getY() * 1.0, self.ds.right_joystick.getY() * 1.0)

    def disabledInit(self) -> None:
        self.dt.stop()

    def disabledPeriodic(self) -> None:
        self.dt.stop()


if __name__ == "__main__":
    wpilib.run(BaseRobot)
