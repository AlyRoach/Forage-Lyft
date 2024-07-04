import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        service_mileage = 0
        engine = CapuletEngine(current_mileage, service_mileage)
        self.assertTrue(engine.needs_service)

    def test_needs_service_false(self):
        current_mileage = 30000
        service_mileage = 0
        engine = CapuletEngine(current_mileage, service_mileage)
        self.assertFalse(engine.needs_service)


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_indicator_on = True
        engine = SternmanEngine(warning_indicator_on)
        self.assertTrue(engine.needs_service)

    def test_needs_service_false(self):
        warning_indicator_on = False
        engine = SternmanEngine(warning_indicator_on)
        self.assertFalse(engine.needs_service)


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60001
        service_mileage = 0
        engine = WilloughbyEngine(current_mileage, service_mileage)
        self.assertTrue(engine.needs_service)

    def test_needs_service_false(self):
        current_mileage = 60000
        service_mileage = 0
        engine = WilloughbyEngine(current_mileage, service_mileage)
        self.assertFalse(engine.needs_service)