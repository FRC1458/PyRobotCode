import numpy as np

from wpilib import Encoder


# TODO Check angle constrain function
def constrain_angle(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


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

    def __init__(self, left_encoder, right_encoder):
        self.left_encoder = left_encoder
        self.right_encoder = right_encoder

    def start(self, reset_encoders=True):
        if reset_encoders:
            self.right_encoder.reset()
            self.left_encoder.reset()
    # TODO FINISH!!!
    def update(self):
        pass
