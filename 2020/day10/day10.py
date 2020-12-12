# https://adventofcode.com/2020/day/10

from collections import defaultdict


def find_joltage_distribution(adapters):
    """Given a list of adapters' ratings in the order they are connected,
    return the number of adapters that have a 1-jolt difference from the
    previous adapter, and the number of adapters that have a 3-jolt difference.
    """
    prev_rating = 0  # Charging outlet rating
    one_jolt = []
    three_jolt = []

    for adapter in adapters:
        jolt_difference = adapter - prev_rating

        if jolt_difference == 1:
            one_jolt.append(adapter)
        elif jolt_difference == 3:
            three_jolt.append(adapter)

        prev_rating = adapter

    three_jolt.append(max(adapters) + 3)  # Device adapter rating

    return len(one_jolt), len(three_jolt)


def find_arrangements(adapters):
    """Given a list of adapters' ratings, returns the number of distinct ways
    to arrange them.

    Adapted from /u/digtydoo's solution
    https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfcxuxf/
    """
    adapters.insert(0, 0)
    arrangements = defaultdict(int)
    arrangements[0] = 1  # Only one arrangement to connect to outlet

    for adapter in adapters:
        for delta in range(1, 4):
            # Different of joltage is between 1 and 3
            valid_adapter = adapter + delta

            if valid_adapter in adapters:
                # Add number of arrangements of current adapter to number of
                # arrangements to get to next valid adapter
                arrangements[valid_adapter] += arrangements[adapter]

    return arrangements[max(adapters)]


if __name__ == "__main__":
    filename = "test.txt"
    with open(filename, "r") as inputf:
        adapters = [int(line) for line in inputf]

    # Sort adapters in order of rating, outlet --> device
    adapters.sort()

    num_1jolt, num_3jolt = find_joltage_distribution(adapters)
    print(f"Part 1: {num_1jolt * num_3jolt}")  # 2232

    print(f"Part 2: {find_arrangements(adapters)}")  # 173625106649344
