from math import sqrt
from pywr.uncertainties.device import Uncertainty, Device


def compute_uncertainty(
    input_value: float, unit_magnitude: float, uncertainty: Uncertainty
):
    normalized_input = input_value * unit_magnitude
    uncertainty = (
        abs(
            (normalized_input * (1 / uncertainty.unit_magnitude))
            * uncertainty.uncertainty
            + (uncertainty.c_constant * uncertainty.dgt_magnitude)
        )
        / sqrt(3)
    ) * uncertainty.unit_magnitude

    return uncertainty * (1 / unit_magnitude)


def uncertainty(
    input_value: float, unit_magnitude: float, device_specs: Device
) -> float:
    normalized_input = input_value * unit_magnitude
    cmp_range_list = [
        (device_specs.probing_specs[i - 1], device_specs.probing_specs[i])
        for i in range(1, len(device_specs.probing_specs))
    ]
    current_uncertainty = next(
        (
            last
            for last, current in cmp_range_list
            if normalized_input >= last.normalized_range
            and normalized_input <= current.normalized_range
        ),
        cmp_range_list[-1][1],
    )

    return compute_uncertainty(input_value, unit_magnitude, current_uncertainty)
