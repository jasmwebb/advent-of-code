# Initialize wire vectors
with open("input.txt", "r") as inputf:
    wires = inputf.readlines()
    wire1 = wires[0].rstrip("\n").split(",")
    wire2 = wires[1].split(",")


def find_coords(wire_vectors):
    """Calcuate each wire's coordinates from a list of vectors.
    Returns a dictionary where the key is the coordinate and the value is
    the step it took to get to that coordinate.
    """
    coords = {}
    x_coord = 0
    y_coord = 0

    for vector in wire_vectors:
        step = int(vector[1:])
        if vector.startswith("L"):
            x_coord -= step
        elif vector.startswith("R"):
            x_coord += step
        elif vector.startswith("D"):
            y_coord -= step
        elif vector.startswith("U"):
            y_coord += step

        coords[(x_coord, y_coord)] = step

    return coords


def find_intersections(wire1, wire2):
    """Iterates through first wire, one pair of coordinates at a time
    (n, n + 1), and second wire in the same way to find points of intersection.
    Each pair of coordinates contains the start and end points of a line.
    Returns a list of tuples containing the coordinates of each intersection.
    """
    wire1_coords = list(wire1.keys())
    wire2_coords = list(wire2.keys())
    intersections = []

    for line1_start, line1_end in zip(wire1_coords[0::1], wire1_coords[1::1]):
        start1_x = line1_start[0]
        start1_y = line1_start[1]
        end1_x = line1_end[0]
        end1_y = line1_end[1]

        for line2_start, line2_end in zip(wire2_coords[0::1], wire2_coords[1::1]):
            start2_x = line2_start[0]
            start2_y = line2_start[1]
            end2_x = line2_end[0]
            end2_y = line2_end[1]

            # If first wire runs vertically (same x-coordinates)
            if start1_x == end1_x:
                # Check if second wire runs horizontally (same y-coordinates)
                if start2_y == end2_y:
                    # Check if first wire's x-coordinate in range of second
                    # wire's start/end x-coordinates (account for line moving
                    # left to right and right to left)
                    if (
                        (start1_x > start2_x and start1_x < end2_x)
                        or (start1_x > end2_x and start1_x < start2_x)
                    ):
                        # Check if second wire's y-coordinate is in range of
                        # first wire's start/end y-coordinates (account for
                        # line moving top-down and bottom-up)
                        if (
                            (start2_y > start1_y and start2_y < end1_y)
                            or (start2_y > end1_y and start2_y < start1_y)
                        ):
                            intersections.append((start1_x, start2_y))
            # Else, first wire runs horizontally (same y-coordinates)
            else:
                # Check if second wire runs vertically
                if start2_x == end2_x:
                    # Check if first wire's y-coordinate is in range of second
                    # wire's start/end y-coordinates
                    if (
                        (start1_y > start2_y and start1_y < end2_y)
                        or (start1_y > end2_y and start1_y < start2_y)
                    ):
                        # Check if second wire's x-coordinate is in range of
                        # first wire's start/end x-coordinates
                        if (
                            (start2_x > start1_x and start2_x < end1_x)
                            or (start2_x > end1_x and start2_x < start1_x)
                        ):
                            intersections.append((start2_x, start1_y))

    return intersections


wire1_coords_step = find_coords(wire1)
wire2_coords_step = find_coords(wire2)
intersections = find_intersections(wire1_coords_step, wire2_coords_step)
manhattan_distances = list(
    map(lambda coord: abs(coord[0]) + abs(coord[1]), intersections[1:])
)

print(
    f"Part 1 Answer: {min(manhattan_distances)}\n"
    f"Part 2 Answer:"
)
# part 2 answer: 101386
