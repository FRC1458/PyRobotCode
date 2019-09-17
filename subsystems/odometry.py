from math import cos, sin, pi

from wpilib import Encoder
from navx import AHRS


# TODO Check angle constrain function
def constrain_angle(x):
    return (x + pi) % (2 * pi) - pi


class Pose2D(object):
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = constrain_angle(theta)

    @staticmethod  # TODO Maybe should just be a function not in a class
    def linear_interp(pose0, pose1, ratio=1.0):
        # TODO literally just rotation matrix rn, change to some probabalistic sampling later
        return Pose2D(pose0.x + ((pose1.x - pose0.x) * ratio), pose0.y + ((pose1.y - pose0.y) * ratio),
                      constrain_angle(pose0.theta + ((pose1.theta - pose0.theta) * ratio)))


class EncoderOdometry(object):
    left_encoder: Encoder
    right_encoder: Encoder
    gyro: AHRS

    def __init__(self, left_encoder, right_encoder, gyro, starting_pose=Pose2D(x=0.0, y=0.0, theta=0.0)):
        self.left_encoder = left_encoder
        self.right_encoder = right_encoder
        self.gyro = gyro

        self.pose = starting_pose

        self.last_left = 0.0
        self.left = 0.0
        self.last_right = 0.0
        self.right = 0.0

    def reset(self, pose=Pose2D(x=0.0, y=0.0, theta=0.0)):
        self.pose = pose

        self.last_left = 0.0
        self.last_right = 0.0

    def setup(self, reset_encoders=True):
        if reset_encoders:
            self.right_encoder.reset()
            self.left_encoder.reset()

        self.last_left = self.left_encoder.getDistance()
        self.last_right = self.right_encoder.getDistance()

    # TODO FINISH!!!
    def update(self):
        self.left = self.left_encoder.getDistance()
        self.right = self.right_encoder.getDistance()

        dl = self.left - self.last_left
        dr = self.right - self.last_right

        self.last_left = self.left
        self.last_right = self.right

        fwd = (dl + dr) / 2.0
        gyro_rads = constrain_angle(self.gyro.getFusedHeading() * 0.0174533)
        theta = constrain_angle(gyro_rads)

        self.pose = Pose2D(self.pose.x + fwd * cos(theta), self.pose.y + fwd * sin(theta), gyro_rads)


