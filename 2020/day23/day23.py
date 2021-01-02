# https://adventofcode.com/2020/day/23

def prep_move(cups, move=0):
    """Sets variables necessary to complete a single move."""
    num_cups = len(cups)

    if move >= num_cups:
        move -= num_cups

    current = cups[move]
    current_copy = cups[move]
    start = move + 1
    end = move + 4
    pick_up = cups[start:end]
    num_pick_up = len(pick_up)

    if num_pick_up < 3:
        pick_up += cups[:3 - num_pick_up]

    destination = None

    while destination is None or start <= destination < end:
        current_copy -= 1

        try:
            destination = cups.index(current_copy)
        except ValueError:
            current_copy = max(cups)
            destination = cups.index(current_copy)

    return (pick_up, current, destination, start, end)


def make_move(cups, prep, move):
    """Simulates a single move then returns new cups order."""
    pick_up, current, destination, start, end = prep
    destination += 1

    if destination > start:
        cups[destination:destination] = pick_up
        del cups[start:end]
    else:  # destination < start
        num_cups = len(cups)

        if end > num_cups:
            end -= num_cups
            del cups[start:]
            del cups[:end]
            destination -= 1
        else:
            del cups[start:end]

        cups[destination:destination] = pick_up
        current_i = cups.index(current)

        if current_i != move:
            new_0 = current_i - move
            cups = cups[new_0:] + cups[:new_0]

    return cups


if __name__ == "__main__":
    cups = [int(n) for n in "942387615"]

    for move in range(1):
        prep = prep_move(cups, move)
        make_move(cups, prep)
