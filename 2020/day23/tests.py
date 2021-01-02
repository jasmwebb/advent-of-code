import unittest
import day23


class TestPlay(unittest.TestCase):
    """Tests for correct simulation of the cup game with the crab."""

    def setUp(self):
        self.cups = [int(n) for n in "389125467"]

    def test_move(self):
        """Tests for correct new cup order for 10 moves."""
        expected_orders = {
            0: [2, 8, 9, 1, 5, 4, 6, 7, 3],
            1: [5, 4, 6, 7, 8, 9, 1, 3, 2],
            2: [8, 9, 1, 3, 4, 6, 7, 2, 5],
            3: [4, 6, 7, 9, 1, 3, 2, 5, 8],
            4: [1, 3, 6, 7, 9, 2, 5, 8, 4],
            5: [9, 3, 6, 7, 2, 5, 8, 4, 1],
            6: [2, 5, 8, 3, 6, 7, 4, 1, 9],
            7: [6, 7, 4, 1, 5, 8, 3, 9, 2],
            8: [5, 7, 4, 1, 8, 3, 9, 2, 6],
            9: [8, 3, 7, 4, 1, 9, 2, 6, 5]
        }
        cups = self.cups[:]

        for move, order in expected_orders.items():
            cups = day23.make_move(cups)

            with self.subTest():
                self.assertEqual(order, cups, msg=f"Failed on Move {move + 2}")

    def test_final(self):
        """Tests for correct final order string after 100 moves."""
        cups = self.cups[:]

        for move in range(100):
            cups = day23.make_move(cups)

        self.assertEqual = ("67384529", day23.stringify(cups))


if __name__ == "__main__":
    unittest.main()
