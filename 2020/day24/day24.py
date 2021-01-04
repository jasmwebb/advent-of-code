# https://adventofcode.com/2020/day/24

from collections import defaultdict, Counter
from re import compile


step_deltas = {
    "e": (-1, 0),
    "se": (0, 1),
    "sw": (1, 1),
    "w": (1, 0),
    "nw": (0, -1),
    "ne": (-1, -1)
}


def find_tile(directions):
    """Follows given directions to find the coordinates of the single tile to
    be flipped."""
    x, y = 0, 0

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


def daily_flip(black_tiles):
    """Flips tiles according to exhibit rules once per day."""
    neighbor_deltas = tuple(step_deltas.values())

    # Caculate all black tiles' neighbors
    # Each time calculated -> +1 black tile immediately adjacent
    neighbors = Counter((x + dx, y + dy)
                        for x, y in black_tiles for dx, dy in neighbor_deltas)

    # Black tiles stay black if neighbors == 1 or 2 (0 or 3+ become white)
    # White tiles become black if neighbors == 2
    black_tiles = tuple(tile for tile, n_nghbr in neighbors.items()
                        if n_nghbr == 2
                        or (tile in black_tiles and n_nghbr == 1))

    return black_tiles


if __name__ == "__main__":
    black = flip_tiles("input.txt")
    print("Part 1:", sum(black.values()))  # 521

    black = tuple(tile for tile, flipped in black.items() if flipped)
    for _ in range(100):
        black = daily_flip(black)

    print("Part 2:", len(black))  # 4242
