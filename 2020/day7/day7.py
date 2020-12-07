# https://adventofcode.com/2020/day/7

from itertools import repeat


def get_rules(file):
    """Create a dictionary from given rules."""
    rules_dict = {}

    with open(file, "r") as inputf:
        for line in inputf:
            color, inner_bags = line.split(" bags contain ")
            inner_bags = inner_bags.rstrip(".\n").split(", ")
            if "no other bags" in inner_bags:
                rules_dict[color] = {}
            else:
                rules_dict[color] = {}
                for bags in inner_bags:
                    inner_color = (
                        bags[2:]
                        .replace(" bags", "")
                        .replace(" bag", "")
                    )
                    rules_dict[color][inner_color] = int(bags[0])

    return rules_dict


def find_outermost_bag(rules: dict, bag_color: list) -> list:
    """Find all valid outermost bag colors for given bag color.
    May contain duplicate colors.
    """
    target_colors = set(bag_color)
    outer_bags = set()

    for color_rule, inner_bags in rules.items():
        for color in inner_bags.keys():
            if color in target_colors:
                outer_bags.add(color_rule)

    outer_bags = list(outer_bags)

    if not outer_bags:
        return outer_bags
    else:
        return outer_bags + find_outermost_bag(rules, outer_bags)


def find_inner_bags(rules: dict, bag_color: list) -> int:
    """Find how many individual bags are required inside of given bag color."""
    inner_bag_colors = []

    for color in bag_color:
        for inner_color, inner_num in rules[color].items():
            inner_bag_colors += list(repeat(inner_color, inner_num))

    num_bags = len(inner_bag_colors)

    if not num_bags:
        return num_bags
    else:
        return num_bags + find_inner_bags(rules, inner_bag_colors)


if __name__ == "__main__":
    input_file = "input.txt"
    my_bag_color = ["shiny gold"]
    bag_rules = get_rules(input_file)

    outermost_bags = find_outermost_bag(bag_rules, my_bag_color)
    print(f"Part 1: {len(set(outermost_bags))}")  # 268

    inner_bags = find_inner_bags(bag_rules, my_bag_color)
    print(f"Part 2: {inner_bags}")  # 7867
