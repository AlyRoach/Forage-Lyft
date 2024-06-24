from engine import Engine 

class CapuletEngine(Engine):
    def __init__(self, current_mileage, service_mileage):
        super().__init__(current_mileage, service_mileage)
        self.current_mileage = current_mileage
        self.service_mileage = service_mileage

    def engine_needs_service(self):
        return self.current_mileage - self.service_mileage > 30000
