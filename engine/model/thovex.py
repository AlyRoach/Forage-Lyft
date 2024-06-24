from car import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin import NubbinBattery


class Thovex(Car):
    def __init__(self, current_mileage, service_mileage, service_date):
        thovex_engine = CapuletEngine(current_mileage,service_mileage)
        thovex_battery = NubbinBattery(service_date)

        super(). __init__(thovex_engine, thovex_battery)

        self.engine = thovex_engine
        self.battery = thovex_battery

    def needs_service(self):
        return super().needs_service()