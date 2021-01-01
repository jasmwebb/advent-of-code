import unittest
import day22
from collections import deque
from copy import deepcopy


class TestPlay(unittest.TestCase):
    """Tests for correct simulation of the card game Combat."""

    def setUp(self):
        self.decks = day22.parse_decks("test.txt")
        self.winner = day22.play_game(deepcopy(self.decks))

    def test_decks(self):
        """Tests for correct input parsing."""
        expected = (deque((9, 2, 6, 3, 1)), deque((5, 8, 4, 7, 10)))
        self.assertEqual(expected, self.decks)

    def test_rounds(self):
        """Tests for proper play for a selection of rounds."""
        decks = deepcopy(self.decks)
        end_of_round = {
            0: (deque((2, 6, 3, 1, 9, 5)), deque((8, 4, 7, 10))),
            1: (deque((6, 3, 1, 9, 5)), deque((4, 7, 10, 8, 2))),
            2: (deque((3, 1, 9, 5, 6, 4)), deque((7, 10, 8, 2))),
            3: (deque((1, 9, 5, 6, 4)), deque((10, 8, 2, 7, 3))),
            26: (deque((4, 1)), deque((9, 7, 3, 2, 10, 6, 8, 5))),
            27: (deque((1,)), deque((7, 3, 2, 10, 6, 8, 5, 9, 4)))
        }

        for round in range(28):
            decks = day22.play_round(decks)
            if round in end_of_round:
                with self.subTest(round=round):
                    self.assertEqual(end_of_round[round], decks)

    def test_winner(self):
        """Checks that full gameplay function returns the expected winner."""
        expected = (1, deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1]))
        self.assertEqual(expected, self.winner)

    def test_score(self):
        """Tests for proper score calculation at the end of the game."""
        self.assertEqual(306, day22.calculate_score(self.winner[1]))


if __name__ == "__main__":
    unittest.main()
