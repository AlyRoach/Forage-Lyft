from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin import NubbinBattery


class Rorschach(Car):
    def __init__(self, current_mileage, service_mileage, service_date):
        rorschach_engine = WilloughbyEngine(current_mileage,service_mileage)
        rorschach_battery = NubbinBattery(service_date)

        super(). __init__(rorschach_engine, rorschach_battery)

        self.engine = rorschach_engine
        self.battery = rorschach_battery

    def needs_service(self):
        return super().needs_service()
