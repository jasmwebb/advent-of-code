# https://adventofcode.com/2020/day/12

from math import prod


class Ship:
    def __init__(self, instructions, ship_start, waypoint_start):
        self.instructions = instructions
        self.ship_direction, self.ship_coord = ship_start
        self.waypoint = waypoint_start
        self.movement = {"E": (1, 0), "S": (0, -1), "W": (-1, 0), "N": (0, 1)}
        self.turn = {"R": 1, "L": -1}
        self.manhattan_distance = 0

    def set_Manhattan(self):
        """Calculates and returns the ships's Manhattan distance from starting
        point to ending point.
        """
        self.manhattan_distance = sum(abs(x) for x in self.ship_coord)

    def move_ship(self):
        """Moves the ship according to instructions.
        Sets Manhattan distance from starting point to ending point.
        """
        cardinals = tuple(self.movement)

        for action, units in self.instructions:
            if action in self.turn:
                rotate = (
                    self.turn[action] * int(units / 90)
                    + cardinals.index(self.ship_direction)
                )
                if rotate >= 4:  # len(cardinals)
                    rotate -= 4
                self.ship_direction = cardinals[rotate]
            else:
                direction = self.ship_direction if action == "F" else action
                move = (units * x for x in self.movement[direction])
                self.ship_coord = tuple(
                    sum(x) for x in zip(self.ship_coord, move)
                )

        self.set_Manhattan()

    def move_waypoint(self):
        """Moves the waypoint according to instructions, relative to the ship,
        then moves the ship to the waypoint.
        Sets the ship's Manhattan distance from starting point to ending point.
        """
        calc_move = lambda coord, d: (d * x for x in coord)
        translate_coord = lambda coord, d: tuple(sum(x) for x in zip(coord, d))
        rotate = {
            90: (lambda coord: tuple(prod(x) for x in zip(coord, (-1, 1)))[::-1]),
            180: (lambda coord: tuple(prod(x) for x in zip(coord, (-1, -1)))),
            270: (lambda coord: tuple(prod(x) for x in zip(coord, (1, -1)))[::-1]),
            -90: (lambda coord: tuple(prod(x) for x in zip(coord, (1, -1)))[::-1]),
            -180: (lambda coord: tuple(prod(x) for x in zip(coord, (-1, -1)))),
            -270: (lambda coord: tuple(prod(x) for x in zip(coord, (-1, 1)))[::-1])
        }

        for action, units in self.instructions:
            # F moves ship to waypoint `units` times, waypoint stays in place
            if action == "F":
                move = calc_move(self.waypoint, units)
                self.ship_coord = translate_coord(self.ship_coord, move)
            # NESW moves waypoint, ship stays in place
            if action in self.movement:
                move = calc_move(self.movement[action], units)
                self.waypoint = translate_coord(self.waypoint, move)
            # LR rotates waypoint, ship stays in place
            if action in self.turn:
                self.waypoint = rotate[units * self.turn[action]](self.waypoint)

        self.set_Manhattan()


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, "r") as inputf:
        instructions = [(line[0], int(line.rstrip()[1:])) for line in inputf]

    start_position = ["E", (0, 0)]
    ferry = Ship(instructions, start_position, (10, 1))

    ferry.move_ship()
    print(f"Part 1: {ferry.manhattan_distance}")  # 1319

    ferry.ship_direction, ferry.ship_coord = start_position
    ferry.move_waypoint()
    print(f"Part 2: {ferry.manhattan_distance}")  # 62434
