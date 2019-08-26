from collections import deque
import logging
from wpilib import Compressor, Solenoid, AnalogInput, Timer

logging.basicConfig(level=logging.DEBUG)


class Pneumatics(object):
    def __init__(self, compressor: Compressor, closed_loop: bool = False, vent_solenoid: Solenoid or None = None,
                 pressure_sensor: AnalogInput or None = None, timer: Timer = Timer()):
        self.timer = timer

        self.compressor = compressor
        self.compressor.setClosedLoopControl(on=closed_loop)

        self.vent_solenoid = vent_solenoid
        self.pressure_sensor = pressure_sensor

        self.pressure_observations = deque(maxlen=10)
        self.last_interval = 0.0
        self.obs_interval_sec = 1.0

    def start_compressor(self):
        self.compressor.start()

    def stop_compressor(self):
        self.compressor.stop()

    def toggle_vent(self):
        if self.vent_solenoid is not None and self.vent_solenoid.get() is False:
            self.vent_solenoid.set(True)

        elif self.vent_solenoid is not None and self.vent_solenoid.get() is True:
            self.vent_solenoid.set(False)

    def get_psi(self):
        # FIXME check math
        psi = (((250.0 * self.pressure_sensor.getVoltage()) / 5.0) - 25.0)
        return psi

    def update_pressure(self):
        # TODO CHECK TIME!!! AND ADD SOME HIGH QUALITY TIMESTAMPS (assume 1 sec rn)
        ts_sec = self.timer.getFPGATimestamp()

        if

        self.pressure_observations.append((((250.0 * self.pressure_sensor.getVoltage()) / 5.0) - 25.0))


