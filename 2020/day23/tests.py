import unittest
import day23


class TestPlay(unittest.TestCase):
    """Tests for correct simulation of the cup game with the crab."""

    def setUp(self):
        self.cups = [int(n) for n in "389125467"]
        self.prep1 = day23.prep_move(self.cups)

    def test_prep(self):
        """Tests for correct preparation for the first move."""
        expected = ([8, 9, 1], 3, 4, 1, 4)
        self.assertEqual(expected, self.prep1)

    def test_move(self):
        """Tests for correct new cup order for 10 moves."""
        expected_orders = {
            0: [3, 2, 8, 9, 1, 5, 4, 6, 7],
            1: [3, 2, 5, 4, 6, 7, 8, 9, 1],
            2: [7, 2, 5, 8, 9, 1, 3, 4, 6],
            3: [3, 2, 5, 8, 4, 6, 7, 9, 1],
            4: [9, 2, 5, 8, 4, 1, 3, 6, 7],
            5: [7, 2, 5, 8, 4, 1, 9, 3, 6],
            6: [8, 3, 6, 7, 4, 1, 9, 2, 5],
            7: [7, 4, 1, 5, 8, 3, 9, 2, 6],
            8: [5, 7, 4, 1, 8, 3, 9, 2, 6],
            9: [5, 8, 3, 7, 4, 1, 9, 2, 6]
        }
        cups = self.cups[:]

        for move, order in expected_orders.items():
            prep = day23.prep_move(cups, move)
            cups = day23.make_move(cups, prep, move)

            with self.subTest():
                self.assertEqual(order, cups, msg=f"Failed on Move {move + 1}")


if __name__ == "__main__":
    unittest.main()
