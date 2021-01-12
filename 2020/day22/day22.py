# https://adventofcode.com/2020/day/22

from collections import deque
from itertools import islice
from math import prod
from operator import itemgetter


def parse_decks(filename):
    """Parses input into two deques representing each player's card deck."""
    with open(filename, "r") as inputf:
        decks = inputf.read().split("\n\n")

    return tuple(
        map(lambda deck: deque(map(int, deck.splitlines()[1:])), decks)
    )


def play_game(player_decks):
    """Simulates the card game Combat from start to end, that is, until one of
    the player's decks is empty.
    Returns the index of the winning deck (player), and the deck itself.
    """
    while all(player_decks):
        plays = (player_decks[0].popleft(), player_decks[1].popleft())
        winner, high_card = max(enumerate(plays), key=itemgetter(1))
        player_decks[winner].extend((high_card, min(plays)))

    return max(enumerate(player_decks), key=itemgetter(1))


def play_recursive(player_decks):
    """Simulates Recursive Combat card game."""
    previous_decks = set()

    while all(player_decks):
        current_decks = tuple(player_decks[0]), tuple(player_decks[1])
        if current_decks in previous_decks:  # base case
            return (0, player_decks[0])

        previous_decks.add(current_decks)
        plays = (player_decks[0].popleft(), player_decks[1].popleft())

        if (len(player_decks[0]) >= plays[0]
            and len(player_decks[1]) >= plays[1]):
            sub_decks = (deque(islice(player_decks[0], 0, plays[0])),
                         deque(islice(player_decks[1], 0, plays[1])))
            winner = play_recursive(sub_decks)[0]
        else:
            winner = max(enumerate(plays), key=itemgetter(1))[0]

        player_decks[winner].extend((plays[winner], plays[int(not winner)]))

    return max(enumerate(player_decks), key=itemgetter(1))


def calculate_score(winning_deck):
    """Calculates score from winner's deck."""
    return sum(
        prod((i + 1, card)) for i, card in enumerate(reversed(winning_deck))
    )


if __name__ == "__main__":
    decks = parse_decks("input.txt")
    winner = play_game(decks)
    print("Part 1:", calculate_score(winner[1]))  # 33473

    decks = parse_decks("input.txt")
    winner = play_recursive(decks)
    print("Part 2:", calculate_score(winner[1]))  # 31793
