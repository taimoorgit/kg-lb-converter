import sys


KG_TO_LB = 2.2046226218
LB_TO_KG = 0.45359237
G_TO_OZ = 0.03527396194958041
OZ_TO_G = 28.349523125
MG_TO_OZ = 0.00003527396194958041
OZ_TO_MG = 28349.523125
ML_TO_FL_OZ = 0.033814022701843
FL_OZ_TO_ML = 29.5735295625
L_TO_GAL = 0.26417205235815
GAL_TO_L = 3.785411784
NG_DL_TO_NMOL_L = 0.03467
NMOL_L_TO_NG_DL = 28.84
KM_TO_MI = 0.62137119223733
MI_TO_KM = 1.609344
M_TO_FT = 3.280839895013123
FT_TO_M = 0.3048
CM_TO_IN = 0.39370078740157477
IN_TO_CM = 2.54


def print_pair(
    value: float,
    metric_unit: str,
    imperial_unit: str,
    metric_to_imperial: float,
    imperial_to_metric: float,
    imperial_precision: int = 2,
    metric_precision: int = 2,
) -> None:
    print(
        f"{value:g} {metric_unit} = "
        f"{value * metric_to_imperial:.{imperial_precision}f} {imperial_unit}"
    )
    print(
        f"{value:g} {imperial_unit} = "
        f"{value * imperial_to_metric:.{metric_precision}f} {metric_unit}"
    )
    print()


def print_temperature_pair(value: float) -> None:
    print(f"{value:g} C = {(value * 9 / 5) + 32:.2f} F")
    print(f"{value:g} F = {(value - 32) * 5 / 9:.2f} C")
    print()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: converter <value>")
        return 1

    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Value must be a number.")
        return 1

    print_pair(value, "kg", "lb", KG_TO_LB, LB_TO_KG)
    print_pair(value, "g", "oz", G_TO_OZ, OZ_TO_G)
    print_pair(value, "mg", "oz", MG_TO_OZ, OZ_TO_MG, imperial_precision=6)
    print_pair(value, "mL", "fl oz", ML_TO_FL_OZ, FL_OZ_TO_ML)
    print_pair(value, "L", "gal", L_TO_GAL, GAL_TO_L)
    print_pair(value, "ng/dL", "nmol/L", NG_DL_TO_NMOL_L, NMOL_L_TO_NG_DL)
    print_pair(value, "km", "mi", KM_TO_MI, MI_TO_KM)
    print_pair(value, "m", "ft", M_TO_FT, FT_TO_M)
    print_pair(value, "cm", "in", CM_TO_IN, IN_TO_CM)
    print_temperature_pair(value)
    return 0
