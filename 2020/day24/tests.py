import unittest
import day24


class Test_Tiles(unittest.TestCase):
    """Tests for simulating laying hexagonal tiles."""

    def setUp(self):
        self.filename = "test.txt"
        self.black = day24.flip_tiles(self.filename)

    def test_flip(self):
        """Tests that the correct amount of tiles are flipped after following
        layout directions. (Part 1)
        """
        self.assertEqual(10, sum(self.black.values()))

    def test_daily_flip(self):
        """Tests that the correct amount of tiles are flipped after 100 days of
        being a living art exhibit. (Part 2)
        """
        black = tuple(tile for tile, flipped in self.black.items() if flipped)

        for _ in range(100):
            black = day24.daily_flip(black)

        self.assertEqual(2208, len(black))


if __name__ == "__main__":
    unittest.main()
