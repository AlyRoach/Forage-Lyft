from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler import SpindlerBattery


class Glissade(Car):
    def __init__(self, current_mileage, service_mileage, service_date):
        glissade_engine = WilloughbyEngine(current_mileage,service_mileage)
        glissade_battery = SpindlerBattery(service_date)

        super(). __init__(glissade_engine, glissade_battery)

        self.engine = glissade_engine
        self.battery = glissade_battery

    def needs_service(self):
        return super().needs_service()
