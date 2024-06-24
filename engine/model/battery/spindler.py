from datetime import datetime
from battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, service_date) -> None:
        super().__init__(service_date)
        self.service_date = service_date

    def battery_needs_service(self):
        service_threshold_date = self.service_date.replace(year=self.service_date + 3)

        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False