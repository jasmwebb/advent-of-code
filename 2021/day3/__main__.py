# https://adventofcode.com/2021/day/3

import sys

from collections import Counter


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


def get_gamma_rate(diagnostic):
    # Zip up the nth element in each line
    bits_by_position = zip(*diagnostic)

    # Construct new binary literal from the most common bit in each position
    return int("".join(
        Counter(bits).most_common(1)[0][0] for bits in bits_by_position
    ), 2)


def get_epsilon_rate(gamma_rate):
    # Invert bits - lol I don't understand numbers enough to programmatically
    # determine the approprate bitmask to use - test input needed 0xF
    return ~gamma_rate & 0xFFF


def get_life_support_factor(type, diagnostic):
    diagnostic = diagnostic
    iteration = 0

    # While there is more than one number in the diagnostic
    # and current iteration number is within bounds
    while len(diagnostic) > 1 and iteration < len(diagnostic[0]):
        bits_in_position = tuple(zip(*diagnostic))[iteration]
        bits_count = Counter(bits_in_position)
        determiner = (
            (
                '1' if bits_count['1'] == bits_count['0']
                else max(bits_count, key=bits_count.get)
            )
            if type == "oxygen" else
            (
                '0' if bits_count['1'] == bits_count['0']
                else min(bits_count, key=bits_count.get)
            )
        )

        # Filter numbers with the most/least common bit in the i-th position
        diagnostic = [
            number for number in diagnostic
            if number[iteration] == determiner
        ]

        iteration += 1

    return int(diagnostic[0], 2)


if __name__ == "__main__":
    input_path = get_input()

    with open(input_path, "r") as inputf:
        diagnostic = [line.rstrip() for line in inputf]

    gamma_rate = get_gamma_rate(diagnostic)
    epsilon_rate = get_epsilon_rate(gamma_rate)

    print(f"Part 1: {gamma_rate * epsilon_rate}")  # 3969000

    oxygen_generator_rating = get_life_support_factor("oxygen", diagnostic)
    co2_scrubber_rating = get_life_support_factor("o2", diagnostic)

    print(f"Part 2: {oxygen_generator_rating * co2_scrubber_rating}")  # 4267809
