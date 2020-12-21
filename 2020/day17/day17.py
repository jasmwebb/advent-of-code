# https://adventofcode.com/2020/day/17

from copy import deepcopy
from itertools import product


def generate_neighbors(coord, deltas):
    """Generates the coordinates of all 26 possible neighbors for a given
    coordinate.
    """
    x, y, z = coord

    for dx, dy, dz in deltas:
        yield (x + dx, y + dy, z + dz)


def count_active(neighbors):
    """Counts and returns the number of active neighbors."""
    active_neighbors = 0
    for neighbor in neighbors:
        active_neighbors += cube_coords.get(neighbor, False)

    return active_neighbors


if __name__ == "__main__":
    # Create coordinates for each char in input (x, y, z, status)
    with open("input.txt", "r") as inputf:
        cube_coords = {
            (x, y, 0): cube == "#"  # Initial z = 0, value: cube status
            for y, line in enumerate(inputf)
            for x, cube in enumerate(line.rstrip())
        }

    # List all neighbor deltas, ignoring (0, 0, 0)
    neighbor_deltas = list(product((0, 1, -1), repeat=3))[1:]
    neighbor_deltas.sort(key=lambda d: d[2])
    manipulated_coords = deepcopy(cube_coords)
    cycle = 0

    while cycle < 6:
        # Add neighbors to cube_coords
        for cube in cube_coords:
            neighbors = generate_neighbors(cube, neighbor_deltas)
            for neighbor in neighbors:
                if neighbor not in cube_coords:
                    manipulated_coords[neighbor] = False

        cube_coords = deepcopy(manipulated_coords)

        # Check each cube
        for cube, status in cube_coords.items():
            neighbors = generate_neighbors(cube, neighbor_deltas)
            active_neighbors = count_active(neighbors)

            # Apply rules
            if (
                (status and not (2 <= active_neighbors <= 3))
                or (not status and active_neighbors == 3)
            ):
                manipulated_coords[cube] = not status

        cube_coords = deepcopy(manipulated_coords)
        cycle += 1

    print(f"Print 1: {sum(cube_coords.values())}")  # 267
