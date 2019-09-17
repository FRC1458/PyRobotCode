import logging

from wpilib import PowerDistributionPanel


class PowerElectronics(object):
    pdp: PowerDistributionPanel

    def __init__(self, channels):
        self.pdp = PowerDistributionPanel(module=0)
        # self.channels = channels

        self.temperature = self.pdp.getTemperature()
        self.voltage = self.pdp.getVoltage()

    def basic_update(self):
        self.temperature = self.pdp.getTemperature()
        self.voltage = self.pdp.getVoltage()

    def check_current(self, channel: int):
        self.basic_update()
        return self.pdp.getCurrent(channel=channel)


