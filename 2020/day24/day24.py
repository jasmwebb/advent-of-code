# https://adventofcode.com/2020/day/24

from collections import defaultdict
from re import compile


def find_tile(directions):
    """Follows given directions to find the coordinates of the single tile to
    be flipped."""
    x, y = 0, 0
    step_deltas = {
        "e": (-1, 0),
        "se": (0, 1),
        "sw": (1, 1),
        "w": (1, 0),
        "nw": (0, -1),
        "ne": (-1, -1)
    }

    for step in directions:
        dx, dy = step_deltas[step]
        x += dx
        y += dy

    return (x, y)


def flip_tiles(filename):
    """Parses input and determines which tiles are flipped to black."""
    black_tiles = defaultdict(lambda: False)

    with open(filename, "r") as inputf:
        regex = compile(r"e|se|sw|w|nw|ne")

        for line in inputf:
            steps = regex.findall(line)
            tile = find_tile(steps)
            black_tiles[tile] = not black_tiles[tile]

    return black_tiles


if __name__ == "__main__":
    black = flip_tiles("input.txt")
    print("Part 1:", sum(black.values()))  # 521
