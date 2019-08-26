import logging
import wpilib

logging.basicConfig(level=logging.DEBUG)


class Power(object):
    def __init__(self):
        self.pdp = wpilib.PowerDistributionPanel(0)
        self.temp = self.pdp.getTemperature()

    def check(self, channel: int):
        temp = self.pdp.getTemperature()
        current = self.pdp.getCurrent(channel=channel)
