# https://adventofcode.com/2020/day/16

from math import prod


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


def discard_invalid_tickets(rules, tickets):
    """Finds and discards tickets that have at least one invalid value.
    Returns a list of valid tickets.
    """
    valid_rngs = [r for rngs in rules.values() for r in rngs]
    invalid_tickets = {
        ticket for ticket in tickets for val in ticket
        if not any((val in rng) for rng in valid_rngs)
    }

    return list(set(tickets) - invalid_tickets)


def determine_fields(rules, tickets):
    """Determines the order fields appear on tickets."""
    field_pos = []
    for field, rngs in rules.items():
        possible_pos = [x for x in range(len(tickets[0]))]

        for ticket in tickets:
            for i, val in enumerate(ticket):
                if not (val in rngs[0] or val in rngs[1]):
                    possible_pos.remove(i)

        field_pos.append(set(possible_pos))

    finalized = []

    while not all(len(pos) == 1 for pos in field_pos):
        finalized_pos = min(pos for pos in field_pos if not (pos in finalized))
        finalized.append(finalized_pos)
        field_pos = [
            pos - finalized_pos if pos != finalized_pos else pos
            for pos in field_pos
        ]

    return dict(zip(rules.keys(), (i for pos in field_pos for i in pos)))


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename, "r") as inputf:
        raw_input = inputf.read().split("\n\n")

    rules, my_ticket, nearby_tickets = parse_input(raw_input)

    print(f"Part 1: {calc_error_rate(rules, nearby_tickets)}")  # 21996

    valid_tickets = discard_invalid_tickets(rules, nearby_tickets)
    fields = determine_fields(rules, valid_tickets)
    answer = prod(
        my_ticket[i] for field, i in fields.items()
        if field.startswith("departure")
    )
    print(f"Part 2: {answer}")  # 650080463519
