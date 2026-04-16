import sys


KG_TO_LB = 2.2046226218487757
LB_TO_KG = 0.45359237


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: converter <value>")
        return 1

    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Value must be a number.")
        return 1

    print(f"{value:g} kg = {value * KG_TO_LB:.2f} lb")
    print(f"{value:g} lb = {value * LB_TO_KG:.2f} kg")
    return 0
