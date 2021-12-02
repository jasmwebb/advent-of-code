import unittest
import day25


class Test_Encryption(unittest.TestCase):
    """Tests simulation of RFID key card and door's cryptographic
    handshake.
    """

    def setUp(self):
        self.card_pub, self.door_pub = day25.parse_input("test.txt")
        self.card_loop = day25.find_loop(self.card_pub)
        self.door_loop = day25.find_loop(self.door_pub)

    def test_find_loop(self):
        """Tests that the correct loop size is calculate for each device."""
        results = (self.card_loop, self.door_loop)
        expected = (8, 11)
        self.assertEqual(expected, results)

    def test_encryptions_match(self):
        """Tests that each encryption key produced matches."""
        card_encryption = day25.transform_key(self.door_pub, self.card_loop)
        door_encryption = day25.transform_key(self.card_pub, self.door_loop)
        self.assertEqual(card_encryption, door_encryption)


if __name__ == "__main__":
    unittest.main()
