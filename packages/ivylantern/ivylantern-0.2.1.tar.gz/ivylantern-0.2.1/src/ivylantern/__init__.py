import argparse
import re

__project_name__ = "ivylantern"

SECONDS_PER_YEAR = int(365.2425 * 24 * 60 * 60)
SECONDS_PER_MONTH = int(SECONDS_PER_YEAR / 12)
SECONDS_PER_WEEK = 7 * 24 * 60 * 60
SECONDS_PER_DAY = 24 * 60 * 60
SECONDS_PER_HOUR = 60 * 60
SECONDS_PER_MINUTE = 60
SECONDS_PER_SECOND = 1


def seconds_to_friendly_duration(total_seconds):
    units = [
        (SECONDS_PER_YEAR, "y"),
        (SECONDS_PER_MONTH, "M"),
        (SECONDS_PER_WEEK, "w"),
        (SECONDS_PER_DAY, "d"),
        (SECONDS_PER_HOUR, "h"),
        (SECONDS_PER_MINUTE, "m"),
        (SECONDS_PER_SECOND, "s"),
    ]

    if total_seconds == 0:
        return "0s"

    parts = []
    for unit_seconds, unit_name in units:
        count = total_seconds // unit_seconds
        if count > 0:
            total_seconds -= count * unit_seconds
            parts.append(f"{count}{unit_name}")

    return "".join(parts)


def friendly_duration_to_seconds(duration):
    seconds_per_unit = {
        "s": SECONDS_PER_SECOND,
        "m": SECONDS_PER_MINUTE,
        "h": SECONDS_PER_HOUR,
        "d": SECONDS_PER_DAY,
        "w": SECONDS_PER_WEEK,
        "M": SECONDS_PER_MONTH,
        "y": SECONDS_PER_YEAR,
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
        seconds = friendly_duration_to_seconds(args.duration)
        print(f"{args.duration} is equal to {seconds} seconds")
        print(f"Formatted duration: {seconds_to_friendly_duration(seconds)}")
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
