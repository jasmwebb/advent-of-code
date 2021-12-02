# https://adventofcode.com/2021/day/1

from sys import argv


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
    filename = argv[1]

    with open(filename, "r") as inputf:
        depth_measurements = [int(line) for line in inputf]

    pair_increases = count_pair_increases(depth_measurements)
    window_increases = count_window_increases(depth_measurements)

    print(f"Part 1: {pair_increases}")  # 1676
    print(f"Part 2: {window_increases}")  # 1706
