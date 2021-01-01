# https://adventofcode.com/2020/day/9

from itertools import combinations


def find_invalid_sum(nums, preamble_n):
    """Finds the first number in given list that is not the sum of two of the
    preamble_n numbers before it and returns its index.
    """
    for i in range(len(nums)):
        addends = nums[i:preamble_n]
        validate_sum = nums[preamble_n]
        invalid_sums = [
            combo for combo in combinations(addends, 2)
            if sum(combo) == validate_sum
        ]

        if not invalid_sums:
            return preamble_n

        preamble_n += 1


def find_weakness(nums, sum_index):
    """Finds encryption weakness in a list of numbers by finding a contiguous
    set of at least two numbers whose sum is the value at the given index.
    """
    nums_range = nums[:sum_index]
    target_sum = nums[sum_index]
    addend_range = 2

    while addend_range <= len(nums_range):
        for i in range(len(nums_range)):
            addends = nums_range[i:addend_range]
            if sum(addends) == target_sum:
                return min(addends) + max(addends)

        addend_range += 1


if __name__ == "__main__":
    filename = "input.txt"
    preamble_len = 25

    with open(filename, "r") as inputf:
        xmas_nums = [int(num) for num in inputf]

    invalid_i = find_invalid_sum(xmas_nums, preamble_len)
    print(f"Part 1: {xmas_nums[invalid_i]}")  # 15353384

    print(f"Part 2: {find_weakness(xmas_nums, invalid_i)}")  # 2466556
