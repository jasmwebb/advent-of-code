# https://adventofcode.com/2020/day/20
# Shout-out to https://github.com/mebeim/aoc/blob/master/2020/README.md#day-20---jurassic-jigsaw

from collections import defaultdict
from itertools import combinations
from math import prod
from operator import itemgetter


def get_edge(tile, side):
    """Find and return given edge of a given tile."""
    if side == "top":
        return tile[0]
    elif side == "bottom":
        return tile[-1]

    # map + itemgetter more performant than generator expr w/ indexing
    elif side == "left":
        return "".join(map(itemgetter(0), tile))
    elif side == "right":
        return "".join(map(itemgetter(-1), tile))


def rotate_tile(tile):
    """Rotates a given tile clockwise. Creates new rows where row-n of the
    newly rotated tile is comprised of the values at index-n of each row in the
    given tile, reversed
    """
    # zipping the unpacked list of tile rows groups values at index-n in each
    # row together
    return tuple("".join(reversed(row) for row in zip(*tile)))


def find_corners():
    """From a dictionary of tiles, determines and returns the IDs of the four
    corner tiles, as well as the sides that are shared with other tiles.
    """
    sides = ("top", "bottom", "left", "right")
    shared_edges = defaultdict(list)

    # Iterate through all combinations of tile pairs
    for id_a, id_b in combinations(tiles, 2):
        tile_a, tile_b = tiles[id_a], tiles[id_b]

        # Tiles can be rotated, check all sides
        for side_a in sides:
            for side_b in sides:
                edge_a = get_edge(tile_a, side_a)
                edge_b = get_edge(tile_b, side_b)

                # Also check if flipped tile matches
                if (
                    edge_a == edge_b
                    or edge_a == edge_b[::-1]
                ):
                    shared_edges[id_a].append(side_a)
                    shared_edges[id_b].append(side_b)

    return {
        tile_id: edges for tile_id, edges in shared_edges.items()
        if len(edges) == 2
    }


def assemble_tiles(corners):
    """Takes list of corners and assembles the rest of tiles around them."""

    # Take one corner and rotate until oriented in top-left position
    # Shared sides rotate to be on the bottom and on the right
    topleft_id, shared_sides = corners.popitem()
    shared_sides = set(shared_sides)
    topleft_tile = tiles[topleft_id]

    if shared_sides == {"top", "right"}:
        topleft_tile = rotate_tile(topleft_tile)
    elif shared_sides == {"top", "left"}:
        topleft_tile = rotate_tile(rotate_tile(topleft_tile))
    elif shared_sides == {"bottom", "left"}:
        topleft_tile = rotate_tile(rotate_tile(rotate_tile(topleft_tile)))

    # Calculate dimensions of final square image
    diagonal = int(len(tiles) ** 0.5)

    return


if __name__ == "__main__":
    # Parse input into dict {id: [tile_str, ...]}
    with open("test.txt", "r") as inputf:
        tiles = {
            int(tile[0][5:-1]): tile[1:]
            for tile in map(str.splitlines, inputf.read().split("\n\n"))
        }

    corners = find_corners()
    print("Part 1:", prod(corners))  # 30425930368573
