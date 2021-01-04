import unittest
import day24


class Test_(unittest.TestCase):
    """Tests for simulating laying hexagonal tiles."""

    def setUp(self):
        self.filename = "test.txt"

    def test_flip(self):
        """Tests that the correct amount of tiles are flipped."""
        black = day24.flip_tiles(self.filename)
        self.assertEqual(10, sum(black.values()))


if __name__ == "__main__":
    unittest.main()
