from math import sqrt
from typing import List, Tuple, Optional

from pydantic import BaseModel


class Uncertainty(BaseModel):
    probe_range: float
    unit_magnitude: float
    uncertainty: float
    c_constant: int
    dgt_magnitude: float

    @property
    def normalized_range(self):
        return self.probe_range * self.unit_magnitude


class Device(BaseModel):
    device_name: str
    desription: Optional[str]
    probing_specs: List[Uncertainty]


if __name__ == "__main__":
    BRYMEN_BM811_VOLTAGE = Device(
        device_name="BrymenB811",
        probing_specs=[
            Uncertainty(
                probe_range=50.0,
                unit_magnitude=0.001,
                uncertainty=0.0012,
                c_constant=2,
                dgt_magnitude=1,
            ),
            Uncertainty(
                probe_range=500,
                unit_magnitude=0.001,
                uncertainty=0.0006,
                c_constant=2,
                dgt_magnitude=1,
            ),
        ],
    )
