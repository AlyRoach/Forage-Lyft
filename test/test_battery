import unittest
from datetime import date

from engine.model.battery.nubbin import NubbinBattery
from engine.model.battery.spindler import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        service_date = date.fromisoformat("2015-05-08")
        battery = NubbinBattery(service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        service_date = date.fromisoformat("2016-05-08")
        battery = NubbinBattery( service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        service_date = date.fromisoformat("2015-05-08")
        battery = SpindlerBattery(service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        service_date = date.fromisoformat("2016-05-08")
        battery = SpindlerBattery(service_date)
        self.assertFalse(battery.needs_service())