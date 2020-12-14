# https://adventofcode.com/2020/day/12

def move_ship(ferry):
    """Moves the ship according to instructions.
    Returns Manhattan distance from starting point to ending point.
    """
    ferry = ["E", (0, 0)]
    movement = {"E": (1, 0), "S": (0, -1), "W": (-1, 0), "N": (0, 1)}
    cardinals = tuple(movement)
    turn = {"R": 1, "L": -1}

    for action, units in instructions:
        if action in turn:
            rotate = turn[action] * int(units / 90) + cardinals.index(ferry[0])
            if rotate >= 4:  # len(cardinals)
                rotate -= 4
            ferry[0] = cardinals[rotate]
        else:
            direction = ferry[0] if action == "F" else action
            move = (units * x for x in movement[direction])
            ferry[1] = tuple(sum(x) for x in zip(ferry[1], move))

    return sum(abs(x) for x in ferry[1])


def move_waypoint(waypoint):
    """Moves waypoint according to instructions, relative to the ship.
    Returns the ship's Manhattan distance from starting point to ending point.
    """
    pass


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, "r") as inputf:
        instructions = [(line[0], int(line.rstrip()[1:])) for line in inputf]

    ferry_start = ["E", (0, 0)]
    print(f"Part 1: {move_ship(ferry_start)}")  # 1319

    waypoint_start = (10, 1)
    move_waypoint(waypoint_start)
