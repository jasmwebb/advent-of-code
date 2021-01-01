# https://adventofcode.com/2020/day/22

from collections import deque
from math import prod
from operator import itemgetter


def parse_decks(filename):
    """Parses input into two deques representing each player's card deck."""
    with open(filename, "r") as inputf:
        decks = inputf.read().split("\n\n")

    return tuple(
        map(lambda deck: deque(map(int, deck.splitlines()[1:])), decks)
    )


def play_round(player_decks):
    """Simulates one round of play and returns the updated player decks."""
    p1, p2 = player_decks
    p1_card = p1.popleft()
    p2_card = p2.popleft()

    if p1_card > p2_card:
        p1.append(p1_card)
        p1.append(p2_card)
    else:  # p2_card > p1_card
        p2.append(p2_card)
        p2.append(p1_card)

    return (p1, p2)


def play_game(player_decks):
    """Simulates the card game Combat from start to end, that is, until one of
    the player's decks is empty.
    Returns the index of the winning deck (player), and the deck itself.
    """
    while all(player_decks):
        player_decks = play_round(player_decks)

    winner, deck = max(enumerate(player_decks), key=itemgetter(1))

    return winner, deck


def calculate_score(winning_deck):
    """Calculates score from winner's deck."""
    deck = reversed(winning_deck)

    return sum(prod((i + 1, card)) for i, card in enumerate(deck))


if __name__ == "__main__":
    decks = parse_decks("input.txt")
    winner = play_game(decks)

    print("Part 1:", calculate_score(winner[1]))  # 33473
