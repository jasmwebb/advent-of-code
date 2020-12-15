# https://adventofcode.com/2020/day/13

from math import ceil


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, "r") as inputf:
        notes = (line for line in inputf)
        timestamp = int(next(notes))
        buses = [int(id) for id in next(notes).split(",") if id != "x"]

    next_stops = [ceil(timestamp / id) * id for id in buses]
    earliest = min(next_stops)
    wait = earliest - timestamp
    next_bus = buses[next_stops.index(earliest)]

    print(f"Part 1: {wait * next_bus}")  # 171
