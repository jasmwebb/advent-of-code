# https://adventofcode.com/2020/day/19

# Shout-out to Marco Bonelli's AoC walkthroughs repo
# https://github.com/mebeim/aoc/blob/master/2020/README.md#day-19---monster-messages

from re import compile


def generate_regex(rule_id=0):
    """Generates regular expression from a dictionary of rules."""
    rule = rules[rule_id]

    # Base case
    if type(rule) is str:
        return rule

    options = []
    for sub in rule:
        option = "".join(generate_regex(option) for option in sub)
        options.append(option)

    return f"({'|'.join(options)})"


def match_looped_rules(string, rule_id=0, i=0):
    """Compares given string to a set of rules. Returns matches.
    Accounts for recursive rules.
    """
    # If we're at the end of the string
    if i >= len(string):
        return []

    rule = rules[rule_id]

    # If rule is "a" or "b"
    if type(rule) is str:
        if string[i] == rule:
            # Return incremented index counter to caller
            return [i + 1]

        # Else, no other matches to make
        return []

    # If rule is sequence, ex: "1 2 3" or "1 2 | 2 1"
    matches = []

    for seq in rule:
        # Start matching from current index
        sub_matches = [i]

        for sub_rule in seq:
            new_matches = []

            for j in sub_matches:
                new_matches += match_looped_rules(string, sub_rule, j)

            sub_matches = new_matches

        matches += sub_matches

    return matches


if __name__ == "__main__":
    with open("input.txt", "r") as inputf:
        rules, messages = inputf.read().split("\n\n")

    messages = tuple(messages.rstrip().split("\n"))

    # Parse rules into dictionary
    rules = [rule.split(": ") for rule in rules.split("\n")]
    rules = {int(k): v.strip('"') for k, v in rules}

    for rule_id, rule in rules.items():
        if rule not in "ab":
            rules[rule_id] = tuple(
                tuple(map(int, rule2.split())) for rule2 in rule.split("|")
            )

    rx = compile(f"^{generate_regex()}$")
    matches = sum(map(bool, map(rx.match, messages)))
    print("Part 1:", matches)  # 248

    # Update rules for Part 2 conditions
    rules[8] = ((42,), (42, 8))
    rules[11] = ((42, 31), (42, 11, 31))

    matches = 0
    for msg in messages:
        matches += len(msg) in match_looped_rules(msg)

    print("Part 2:", matches)  # 381
