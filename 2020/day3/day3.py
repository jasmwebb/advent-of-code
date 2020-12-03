# https://adventofcode.com/2020/day/3

def expand_map(map, slope: tuple) -> list:
    """Expands given map (list of strings) to accomodate given slope.
    Returns the expanded list.
    """
    repeats = round(slope[0] * len(map) / len(map[0])) + 1

    return [row * repeats for row in map]


def find_trees(map, slope: tuple) -> int:
    """Checks if there is a tree (#) along a given slope within a given map
    (list of strings). Returns the number of trees.
    """
    x = slope[0]
    y = slope[1]
    check_pos = x
    tree_count = 0

    for row in map[y::y]:
        if row[check_pos] == "#":
            tree_count += 1

        check_pos += x

    return tree_count


if __name__ == "__main__":
    with open("input.txt", "r") as inputf:
        tree_map = [row.rstrip("\n") for row in inputf]

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_product = 1

    for slope in slopes:
        check_map = expand_map(tree_map, slope)
        found_trees = find_trees(check_map, slope)
        tree_product *= found_trees

    print(f"Part 2: {tree_product}")
