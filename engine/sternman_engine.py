from engine import Engine 

class SternmanEngine(Engine):
    def __init__(self, warning_indicator_on):
        super().__init__(warning_indicator_on)
        self.warning_indicator_on = warning_indicator_on

    def engine_needs_service(self):
        if self.warning_indicator_on:
            return True
        else:
            return False
