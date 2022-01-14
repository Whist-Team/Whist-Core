import unittest

from whist.core.cards.card import Suit


class SuitTestCase(unittest.TestCase):
    def test_suit_order(self):
        self.assertLess(Suit.CLUBS, Suit.DIAMONDS)
        self.assertLess(Suit.DIAMONDS, Suit.HEARTS)
        self.assertLess(Suit.HEARTS, Suit.SPADES)

    def test_by_ordinal(self):
        clubs = Suit(0)
        self.assertEqual(Suit.CLUBS, clubs)

    def test_by_long_name(self):
        clubs = Suit('clubs')
        self.assertEqual(Suit.CLUBS, clubs)

    def test_by_short_name(self):
        clubs = Suit('♣')
        self.assertEqual(Suit.CLUBS, clubs)

    def test_by_name_wrong_key(self):
        with self.assertRaises(ValueError):
            Suit('herz')
