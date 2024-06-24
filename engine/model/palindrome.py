from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler import SpindlerBattery


class Palindrome(Car):
    def __init__(self, warning_indicator_on, service_date):
        palindrome_engine = SternmanEngine(warning_indicator_on)
        palindrome_battery = SpindlerBattery(service_date)

        super(). __init__(palindrome_engine, palindrome_battery)

        self.engine = palindrome_engine
        self.battery = palindrome_battery

    def needs_service(self):
        return super().needs_service()