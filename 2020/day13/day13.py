# https://adventofcode.com/2020/day/13

from math import ceil

if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, "r") as inputf:
        notes = (line for line in inputf)
        timestamp = int(next(notes))
        buses = {
            int(id): i for i, id in enumerate(next(notes).split(","))
            if id != "x"
        }

    next_stops = {(ceil(timestamp / id) * id): id for id in buses}
    earliest = min(next_stops)

    print(f"Part 1: {(earliest - timestamp) * next_stops[earliest]}")  # 171

    """ Part 2 adapted from /u/rhesusfecespieces and /u/Zweedeend's solutions
    https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfqvuh9/
    """
    bus_ids = list(buses.keys())
    time_start = 0
    step = bus_ids[0]  # Check multiples of first bus's ID

    for id in bus_ids[1:]:
        delta = buses[id]
        for time in range(time_start, id * step, step):
            if not (time + delta) % id:  # If not 0
                step *= id
                time_start = time

    print(f"Part 2: {time_start}")  # 539746751134958
