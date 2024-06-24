from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, current_mileage, service_mileage, warning_indicator_on:False) -> None:
        self.current_mileage = current_mileage
        self.service_mileage = service_mileage
        self.warning_indicator_on = warning_indicator_on

        @abstractmethod
        def engine_needs_service(self):
            pass