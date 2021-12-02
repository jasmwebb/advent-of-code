# https://adventofcode.com/2021/day/2

from math import prod
from sys import argv


def get_position(commands):
    horizontal, depth = [], []

    for direction, delta in commands:
        delta = int(delta)

        if direction == "forward":
            horizontal.append(delta)
        else:
            depth.append(delta if direction == "down" else delta * -1)

    return sum(horizontal), sum(depth)


def get_position_with_aim(commands):
    horizontal, depth, aim = 0, 0, 0

    for direction, delta in commands:
        delta = int(delta)

        if direction == "forward":
            horizontal += delta
            depth += delta * aim
        else:
            aim += delta if direction == "down" else delta * -1

    return horizontal, depth


if __name__ == "__main__":
    filename = argv[1]

    with open(filename, "r") as inputf:
        commands = [tuple(line.split()) for line in inputf]

    position = get_position(commands)

    print(f"Part 1: {prod(position)}")  # 1762050

    position = get_position_with_aim(commands)

    print(f"Part 2: {prod(position)}")  # 1855892637
