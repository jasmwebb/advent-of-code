# https://adventofcode.com/2020/day/5

def find_seat(barcode, type):
    """Finds the row or column number of a seat, given the boarding pass's
    barcode.
    """
    if type == "row":
        barcode_chars = barcode[:7]
        check_range = [0, 127]
        lower_char = "F"
    else:  # type == "col"
        barcode_chars = barcode[7:10]
        check_range = [0, 7]
        lower_char = "L"

    for char in barcode_chars:
        # Find midpoint in range
        midpoint = sum(check_range) // 2

        if char == lower_char:
            # "F" (row) or "L" (col), take lower half
            check_range[1] = midpoint
        else:
            # "B" (row) or "R" (col), take upper half
            check_range[0] = midpoint + 1

    return check_range[0]


if __name__ == "__main__":
    with open("input.txt", "r") as inputf:
        passes = [line for line in inputf]

    seat_IDs = []

    for barcode in passes:
        row_num = find_seat(barcode, "row")
        col_num = find_seat(barcode, "col")
        seat_IDs.append(row_num * 8 + col_num)

    print(f"Part 1: {max(seat_IDs)}")  # 922

    for seat in range(min(seat_IDs), max(seat_IDs)):
        if seat not in seat_IDs:
            print(f"Part 2: {seat}")  # 747
