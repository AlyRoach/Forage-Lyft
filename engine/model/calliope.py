from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler import SpindlerBattery


class Calliope(Car):
    def __init__(self, current_mileage, service_mileage, service_date):
        calliope_engine = CapuletEngine(current_mileage,service_mileage)
        calliope_battery = SpindlerBattery(service_date)

        super(). __init__(calliope_engine, calliope_battery)

        self.engine = calliope_engine
        self.battery = calliope_battery

    def needs_service(self):
        return super().needs_service()

