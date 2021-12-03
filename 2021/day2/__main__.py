# https://adventofcode.com/2021/day/2

import sys

from math import prod


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
    input_path = get_input()

    with open(input_path, "r") as inputf:
        commands = [tuple(line.split()) for line in inputf]

    position = get_position(commands)

    print(f"Part 1: {prod(position)}")  # 1762050

    position = get_position_with_aim(commands)

    print(f"Part 2: {prod(position)}")  # 1855892637
