import unittest

from whist.core.cards.card import Suit


class SuitTestCase(unittest.TestCase):
    def test_suit_order(self):
        self.assertLess(Suit.CLUBS, Suit.DIAMONDS)
        self.assertLess(Suit.DIAMONDS, Suit.HEARTS)
        self.assertLess(Suit.HEARTS, Suit.SPADES)

    def test_by_label(self):
        clubs = Suit.by_label('clubs')
        self.assertEqual(Suit.CLUBS, clubs)

    def test_by_short_label(self):
        clubs = Suit.by_label('♣', search_symbols=True)
        self.assertEqual(Suit.CLUBS, clubs)

    def test_by_label_wrong_key(self):
        with self.assertRaises(KeyError):
            Suit.by_label('herz')
