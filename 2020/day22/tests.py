import unittest
import day22
from collections import deque
from copy import deepcopy


class TestPlay(unittest.TestCase):
    """Tests for correct simulation of the card game Combat."""

    def setUp(self):
        self.decks = day22.parse_decks("test.txt")
        self.winner1 = day22.play_game(deepcopy(self.decks))
        self.winner2 = day22.play_recursive(deepcopy(self.decks))

    def test_decks(self):
        """Tests for correct input parsing."""
        expected = (deque((9, 2, 6, 3, 1)), deque((5, 8, 4, 7, 10)))
        self.assertEqual(expected, self.decks)

    def test_game(self):
        """Tests that full non-recursive gameplay returns the expected winner.
        """
        expected = (1, deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1]))
        self.assertEqual(expected, self.winner1)

    def test_recursive(self):
        """Tests that full recursive gameplay returns the expected winner."""
        expected = (1, deque([7, 5, 6, 2, 4, 1, 10, 8, 9, 3]))
        self.assertEqual(expected, self.winner2)

    def test_score(self):
        """Tests for proper score calculation at the end of the game."""
        expected = (306, 291)
        scores = (day22.calculate_score(self.winner1[1]),
                  day22.calculate_score(self.winner2[1]))
        self.assertEqual(expected, scores)


if __name__ == "__main__":
    unittest.main()
