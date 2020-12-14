# https://adventofcode.com/2020/day/11

from collections import Counter
from copy import deepcopy
from itertools import product


class Seats:
    def __init__(self, seat_grid):
        self.rows, self.cols = len(seat_grid), len(seat_grid[0])
        self.seats = seat_grid

    def predict_until_stable(self):
        """Predicts seat occupation until seats stop changing."""
        stable = False

        while not stable:
            last_prediction = deepcopy(self.seats)
            self.predict_seats()
            stable = self.seats == last_prediction

        return

    def predict_seats(self):
        """Iterates through each row of seats, applying rules of occupation.
        Modifies seats in place.
        """
        prediction = deepcopy(self.seats)

        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[row][col] != ".":  # Skip floor space
                    prediction[row][col] = self.apply_rules((row, col))

        self.seats = prediction

        return

    def apply_rules(self, seat):
        """Applies rules that determine if seat is empty or occupied."""
        r, c = seat[0], seat[1]
        seat_val = self.seats[seat[0]][seat[1]]

        # Coordinates of adjacent seats, relative to seat being checked (0, 0)
        adjacent_seats = [
            (r + x, c + y) for x, y in list(product([0, 1, -1], repeat=2))[1:]
        ]

        # Count number of occupied adjacent seats
        adj_occupied = Counter([
            self.seats[adj_row][adj_col] for adj_row, adj_col in adjacent_seats
            if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols
        ])["#"]

        # Empty seat with no adjacent occupied seats becomes occupied
        if seat_val == "L" and not adj_occupied:
            return "#"

        # Occupied seat with 4+ adjacent occupied seats becomes empty
        elif seat_val == "#" and adj_occupied >= 4:
            return "L"

        # Seat doesn't change
        return seat_val

    def count_occupied_seats(self):
        """Counts and returns the number of occupied seats."""
        return Counter(seat for row in self.seats for seat in row)["#"]


if __name__ == "__main__":
    filename = "test.txt"
    with open(filename, "r") as inputf:
        seats = [list(line.rstrip()) for line in inputf]

    seats = Seats(seats)
    seats.predict_until_stable()
    print(f"Part 1: {seats.count_occupied_seats()}")  # 2261
