import unittest
from day21 import parse_ingredients, crossref


class TestInput(unittest.TestCase):
    """Tests for correct input parsing."""

    def setUp(self):
        (self.ingredients,
         self.allergen_linked_to,
         self.foods_containing) = parse_ingredients("test.txt")

    def test_foods(self):
        expected = (
            ("mxmxvkd", "kfcds", "sqjhc", "nhms"),
            ("trh", "fvjkl", "sbzzf", "mxmxvkd"),
            ("sqjhc", "fvjkl"),
            ("sqjhc", "mxmxvkd", "sbzzf")
        )
        self.assertEqual(expected, self.ingredients)

    def test_ingredients(self):
        expected = {
            "mxmxvkd": {"dairy", "fish"},
            "kfcds": {"dairy", "fish"},
            "sqjhc": {"dairy", "fish", "soy"},
            "nhms": {"dairy", "fish"},
            "trh": {"dairy"},
            "fvjkl": {"dairy", "soy"},
            "sbzzf": {"dairy", "fish"}
        }
        self.assertEqual(expected, self.allergen_linked_to)

    def test_allergens(self):
        expected = {
            "dairy": [0, 1],
            "fish": [0, 3],
            "soy": [2]
        }
        self.assertEqual(expected, self.foods_containing)


class TestCrossref(unittest.TestCase):
    """Tests for determining hypoallergenic ingredients."""

    def setUp(self):
        self.test_data = parse_ingredients("test.txt")
        self.hypo, self.occurences = crossref(self.test_data)

    def test_hypoallergenic(self):
        expected = {"kfcds", "nhms", "sbzzf", "trh"}
        self.assertEqual(expected, set(self.hypo))

    def test_counter(self):
        self.assertEqual(5, self.occurences)


if __name__ == '__main__':
    unittest.main()
