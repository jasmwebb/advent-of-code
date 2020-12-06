# https://adventofcode.com/2020/day/6

from collections import Counter


def get_input(file) -> tuple:
    """Reads input file into list of strings containing all group answers.
    Determines the number of people in each group.
    Returns tuple containing the number of people [0] and the answers [1].
    """
    with open(file, "r") as inputf:
        group_answers = [
            group.split() for group in inputf.read().split("\n\n")
        ]

        # Count number of people in each group
        num_people = [len(group) for group in group_answers]

        # Remove newlines between each group member's answers
        group_answers = [
            "".join([answer for answer in group if answer != "\n"])
            for group in group_answers
        ]

        return (num_people, group_answers)


def count_every_yes(members: list, answers: list) -> list:
    """Counts the number of questions everyone in a group answered yes to.
    Returns as a list of integers indicating number of yes's per group.
    """
    members_answers = list(zip(members, answers))
    groups_yes = []

    for group in members_answers:
        num_every_yes = 0

        # Count the number of times a question had a yes answer within group
        for question, num_yes in Counter(group[1]).items():
            if num_yes == group[0]:
                num_every_yes += 1

        groups_yes.append(num_every_yes)

    return groups_yes


if __name__ == "__main__":
    input_file = "input.txt"
    num_group_members, group_answers = get_input(input_file)

    # Find number of questions anyone in group answered yes to
    # Cast each group's answers to set to discount duplicates
    num_any = [len(set(group)) for group in group_answers]
    print(f"Part 1: {sum(num_any)}")  # 6273

    num_every = count_every_yes(num_group_members, group_answers)
    print(f"Part 2: {sum(num_every)}")  # 3254
