from itertools import combinations
from math import prod


def check_sum_give_prod(target_sum, nums):
    """Check if given integers' sum is 2020. If True, return their product."""
    if sum(nums) == target_sum:
        return prod(nums)

    return False


# Read input into list of integers
with open("input.txt", "r") as inputf:
    expenses = list(map(int, inputf.read().split("\n")))

if __name__ == "__main__":
    # Iterate through expenses one pair at a time, ignoring order
    for expense_combo in combinations(expenses, 2):
        check_combo = check_sum_give_prod(2020, expense_combo)
        if check_combo:
            print(f"Part 1: {check_combo}")

    # Iterate 3 at a time, ignoring order
    for expense_combo in combinations(expenses, 3):
        check_combo = check_sum_give_prod(2020, expense_combo)
        if check_combo:
            print(f"Part 2: {check_combo}")
