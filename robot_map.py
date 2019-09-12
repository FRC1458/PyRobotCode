import logging
import time

from wpilib import Encoder, Timer, Talon

from ctre import WPI_TalonSRX, TalonSRX
from navx import AHRS

from subsystems.tank_drivetrain import TankDrivetrain
from subsystems.odometry import EncoderOdometry


class RobotMap(object):
    timer = Timer()

    gyroscope = AHRS.create_i2c()

    left_encoder = Encoder()
    right_encoder = Encoder()

    drivetrain = TankDrivetrain(left_motors=[TalonSRX(10)], right_motors=[TalonSRX(31)])

    odometry = EncoderOdometry(left_encoder=left_encoder, right_encoder=right_encoder, gyro=gyroscope)

    # Interface setup
    def __init__(self):
        for encoder in [self.left_encoder, self.right_encoder]:
            encoder.setMaxPeriod(1.0)
            encoder.setDistancePerPulse(1.0)
            encoder.samplesToAverage = 6
