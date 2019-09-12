import logging
import wpilib


class PowerElectronics(object):
    def __init__(self, channels):
        self.pdp = wpilib.PowerDistributionPanel(module=0)
        self.channels = channels

        self.temperature = self.pdp.getTemperature()
        self.voltage = self.pdp.getVoltage()

    def check(self, channel: int):
        self.temperature = self.pdp.getTemperature()
        self.voltage = self.pdp.getVoltage()

        return self.pdp.getCurrent(channel=channel)


