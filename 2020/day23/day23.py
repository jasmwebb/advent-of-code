# https://adventofcode.com/2020/day/23

from collections import deque


def validate_destination(destination, pick_up_list, cup_list):
    """Determines the value of the destination cup."""
    if destination in pick_up_list:
        return validate_destination(destination - 1, pick_up_list, cup_list)

    if destination < min(cup_list):
        return validate_destination(max(cup_list), pick_up_list, cup_list)

    return destination


def make_move(cups):
    """Sets variables necessary to complete a single move."""
    cups = deque(cups)
    current = cups.popleft()
    pick_up = [cups.popleft() for _ in range(3)]
    cups = list(cups)
    destination = validate_destination(current - 1, pick_up, cups)
    destination = cups.index(destination) + 1
    cups = cups[:destination] + pick_up + cups[destination:] + [current]

    return cups


def stringify(final_order):
    """Creates a string from the final order of cups, starting from (but
    excluding) the cup labelled 1, going clockwise.
    """
    one = final_order.index(1)

    return "".join(map(str, final_order[one + 1:] + final_order[:one]))


if __name__ == "__main__":
    cups = [int(n) for n in "942387615"]

    for move in range(100):
        cups = make_move(cups)

    print("Part 1:", stringify(cups))  # 36542897
