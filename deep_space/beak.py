from wpilib import DoubleSolenoid, Timer

from subsystems.driver_station import DriverStation


class BeakMechanism(object):
    forward = DoubleSolenoid.Value.kForward
    reverse = DoubleSolenoid.Value.kReverse
    off = DoubleSolenoid.Value.kOff

    def __init__(self, beak_solenoid: DoubleSolenoid, diag_solenoid: DoubleSolenoid,
                 driver_station: DriverStation = None, timer: Timer = Timer(), cooldown: float = 0.5):
        self.timer = timer
        self.cooldown = cooldown

        self.driver_station = driver_station

        self.beak_solenoid = beak_solenoid
        self.beak_state = False
        self.beak_last = 0

        self.diag_solenoid = diag_solenoid
        self.diag_state = False
        self.diag_last = 0

    def toggle_beak(self):
        if self.timer.getFPGATimestamp() >= self.beak_last + self.cooldown:
            if self.beak_state is True:
                print("Beak Opened")
                self.beak_solenoid.set(self.forward)
                self.beak_last = self.timer.getFPGATimestamp()

                self.beak_state = False

            elif self.beak_state is False:
                print("Beak Closed")

                self.beak_solenoid.set(self.reverse)
                self.beak_last = self.timer.getFPGATimestamp()
                self.beak_state = True
        return

    def toggle_diag(self):
        if self.timer.getFPGATimestamp() >= self.diag_last + self.cooldown:
            if self.diag_state is True:
                print("Beak Extended")

                self.diag_solenoid.set(self.forward)
                self.diag_last = self.timer.getFPGATimestamp()
                self.diag_state = False

            elif self.diag_state is False:
                print("Beak Retracted")

                self.diag_solenoid.set(self.reverse)
                self.diag_last = self.timer.getFPGATimestamp()
                self.diag_state = True
        return

    def update(self):
        if self.driver_station.controller.getAButton():
            self.toggle_beak()

        elif self.driver_station.controller.getXButton():
            self.toggle_diag()




