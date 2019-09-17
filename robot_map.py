import logging
import time

from wpilib import Timer, Compressor, DoubleSolenoid, XboxController
from ctre import TalonSRX
from navx import AHRS

from subsystems.tank_drivetrain import TankDrivetrain
from subsystems.odometry import EncoderOdometry
from subsystems.pneumatics import Pneumatics
from subsystems.driver_station import DriverStation

from deep_space.beak import BeakMechanism


class RobotMap(object):
    def __init__(self):
        self.timer = Timer()
        self.driver_station = DriverStation(controller=XboxController(0))

        # self.gyroscope = AHRS.create_i2c()

        # self.left_encoder = Encoder()
        # self.right_encoder = Encoder()

        self.drivetrain = TankDrivetrain(timer=self.timer, left_motors=[TalonSRX(10), TalonSRX(6)],
                                         right_motors=[TalonSRX(12), TalonSRX(18)])

        self.pneumatics = Pneumatics(compressor=Compressor(0), start_compressor=True, timer=self.timer)

        self.beak = BeakMechanism(beak_solenoid=DoubleSolenoid(0, 4, 5), diag_solenoid=DoubleSolenoid(0, 0, 1),
                                  driver_station=self.driver_station, timer=self.timer, cooldown=0.5)

        # self.odometry = EncoderOdometry(left_encoder=self.left_encoder, right_encoder=self.right_encoder, gyro=self.gyroscope)

        '''
        # Interface setup
        def __init__(self):
            for encoder in [self.left_encoder, self.right_encoder]:
                encoder.setMaxPeriod(1.0)
                encoder.setDistancePerPulse(1.0)
                encoder.samplesToAverage = 6
        '''
