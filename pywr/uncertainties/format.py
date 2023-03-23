from typing import Tuple
from uncertainties import ufloat
from pywr.uncertainties.device import Device


def rounded_uncertainty_with_nominal_value(
    input_value: float, unit_magnitude: float, device_specs: Device
) -> Tuple[str, str]:
    uncertainty = uncertainty(input_value, unit_magnitude, device_specs)

    rounded_str = "{:.2f}".format(ufloat(input_value, uncertainty))
    rounded_value = rounded_str.split("+/-")[0]
    rounded_uncertainty = rounded_str.split("+/-")[1]

    return rounded_value, rounded_uncertainty
