from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, service_date) -> None:
        self.service_date = service_date

        @abstractmethod
        def battery_needs_service(self):
            pass