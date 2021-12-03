# https://adventofcode.com/2021/day/

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


if __name__ == "__main__":
    input_path = get_input()

    with open(input_path, "r") as inputf:
        pass

    print(f"Part 1: {}")
    print(f"Part 2: {}")
