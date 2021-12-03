# https://adventofcode.com/2021/day/1

import sys


def get_input():
    try:
        if sys.argv[1] == "-t":
            filename = "test"
        else:
            sys.exit(
                f"\n\033[0;33mInvalid flag\033[0;0m, ya dingus."
                f"\n🌼 \033[3;37mDid you mean"
                f"\033[1;35;40m python3 {sys.argv[0]} -t \033[0;0m \033[3;37m"
                f"?\033[0;0m\n"
            )
    except IndexError:
        filename = "input"

    return f"{sys.argv[0]}/{filename}.txt"


def count_pair_increases(measurements):
    return sum(
        measurement_a < measurement_b
        for measurement_a, measurement_b in zip(measurements, measurements[1:])
    )


def count_window_increases(measurements):
    windows = [
        sum(window)
        for window in zip(measurements, measurements[1:], measurements[2:])
    ]

    return count_pair_increases(windows)


if __name__ == "__main__":
    input_path = get_input()

    with open(input_path, "r") as inputf:
        depth_measurements = [int(line) for line in inputf]

    pair_increases = count_pair_increases(depth_measurements)
    window_increases = count_window_increases(depth_measurements)

    print(f"Part 1: {pair_increases}")  # 1676
    print(f"Part 2: {window_increases}")  # 1706
