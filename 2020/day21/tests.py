import unittest
import day21


class TestInput(unittest.TestCase):
    """Tests for correct input parsing."""

    def setUp(self):
        (self.ingredients,
         self.allergens_in,
         self.foods_containing) = day21.parse_ingredients("test.txt")

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
        self.assertEqual(expected, self.allergens_in)

    def test_allergens(self):
        expected = {
            "dairy": [0, 1],
            "fish": [0, 3],
            "soy": [2]
        }
        self.assertEqual(expected, self.foods_containing)


class TestSafe(unittest.TestCase):
    """Tests for determining hypoallergenic ingredients."""

    def setUp(self):
        self.test_data = day21.parse_ingredients("test.txt")
        (self.occurences,
         self.updated_data) = day21.determine_safe(self.test_data)

    def test_hypoallergenic(self):
        expected = {"kfcds", "nhms", "sbzzf", "trh"}
        hypoallergenic = {
            ingredient
            for ingredient, allergens in self.updated_data.items()
            if not len(allergens)
        }
        self.assertEqual(expected, hypoallergenic)

    def test_counter(self):
        self.assertEqual(5, self.occurences)


class TestAllergens(unittest.TestCase):
    """Tests for determining allergenic ingredients."""

    def setUp(self):
        self.test_data = day21.parse_ingredients("test.txt")
        self.updated_data = day21.determine_safe(self.test_data)[1]
        self.allergens = day21.determine_allergens(self.updated_data)

    def test_allergens(self):
        expected = "mxmxvkd,sqjhc,fvjkl"
        self.assertEqual(expected, self.allergens)


if __name__ == '__main__':
    unittest.main()
