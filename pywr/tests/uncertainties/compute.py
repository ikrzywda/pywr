import unittest
from math import isclose
from typing import List
from pydantic import ValidationError
from pywr.uncertainties.device import (
    Uncertainty,
    Device,
    compute_uncertainty,
)


class TestUncertainty(unittest.TestCase):
    def setUp(self):
        self.u1 = Uncertainty(
            probe_range=100.0,
            unit_magnitude=0.001,
            uncertainty=0.01,
            c_constant=1,
            dgt_magnitude=0.01,
        )

    def test_normalized_range(self):
        self.assertAlmostEqual(self.u1.normalized_range, 0.1, places=6)


class TestDevice(unittest.TestCase):
    def setUp(self):
        self.du1 = Device(
            device_name="Test Device",
            desription="This is a test device.",
            probing_specs=[
                Uncertainty(
                    probe_range=100.0,
                    unit_magnitude=0.001,
                    uncertainty=0.01,
                    c_constant=1,
                    dgt_magnitude=0.01,
                ),
                Uncertainty(
                    probe_range=1000.0,
                    unit_magnitude=0.01,
                    uncertainty=0.1,
                    c_constant=2,
                    dgt_magnitude=0.001,
                ),
                Uncertainty(
                    probe_range=10000.0,
                    unit_magnitude=0.1,
                    uncertainty=1.0,
                    c_constant=3,
                    dgt_magnitude=0.0001,
                ),
            ],
        )

    def test_device_name(self):
        self.assertEqual(self.du1.device_name, "Test Device")


if __name__ == "__main__":
    unittest.main()
