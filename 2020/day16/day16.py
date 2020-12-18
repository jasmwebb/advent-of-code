# https://adventofcode.com/2020/day/16

def parse_input(raw_input):
    """Parses input and returns the data as their appropriate data structures.
    """
    raw_rules, my_ticket, nearby_tickets = raw_input

    rules = {}
    for rule in raw_rules.split("\n"):
        field, values = rule.split(": ")
        values = (
            tuple(map(int, vs.split("-"))) for vs in values.split(" or ")
        )

        rules[field] = [range(min(v), max(v) + 1) for v in values]

    my_ticket = tuple(int(x) for x in my_ticket.split("\n")[1].split(","))

    nearby_tickets = [
        tuple(map(int, ticket.split(",")))
        for ticket in nearby_tickets.rstrip().split("\n")[1:]
    ]

    return rules, my_ticket, nearby_tickets


def calc_error_rate(rules, tickets):
    """Calculates ticket scanning error rate. That is, returns the sum of all
    invalid values within a list of tickets.
    """
    valid_rngs = [r for rngs in rules.values() for r in rngs]

    rate = 0
    for val in (v for tup in tickets for v in tup):
        if not any((val in rng) for rng in valid_rngs):
            rate += val

    return rate


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, "r") as inputf:
        raw_input = inputf.read().split("\n\n")

    rules, my_ticket, nearby_tickets = parse_input(raw_input)

    print(f"Part 1: {calc_error_rate(rules, nearby_tickets)}")  # 21996
