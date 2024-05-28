import argparse
import re

__project_name__ = "ivylantern"


def convert_duration(duration):
    seconds_per_unit = {
        "s": 1,
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
        "w": 7 * 24 * 60 * 60,
        "M": int(365.2425 / 12 * 24 * 60 * 60),  # Average
        "y": int(365.2425 * 24 * 60 * 60),  # Average
    }

    pattern = re.compile(r"(\d*\.?\d+)([smhdwMy])")
    matches = pattern.findall(duration)
    if not matches:
        raise ValueError(f"invalid duration format: {duration}")

    total_seconds = 0
    for value, unit in matches:
        if not value:
            value = "1"
        seconds = float(value) * seconds_per_unit[unit]
        total_seconds += seconds

    return int(total_seconds)


def main():
    parser = argparse.ArgumentParser(
        description="Convert user-friendly duration to seconds"
    )
    parser.add_argument(
        "duration", help="Duration in user-friendly format (e.g., 1d3w, 2.5h30m)"
    )
    args = parser.parse_args()

    try:
        seconds = convert_duration(args.duration)
        print(f"{args.duration} is equal to {seconds} seconds")
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
