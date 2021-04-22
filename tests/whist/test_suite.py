import unittest

from whist.card import Suit


class SuitTestCase(unittest.TestCase):
    def test_by_label(self):
        clubs = Suit.by_label('clubs')
        self.assertEqual(Suit.CLUBS, clubs)

    def test_by_short_label(self):
        clubs = Suit.by_label('♣', search_symbols=True)
        self.assertEqual(Suit.CLUBS, clubs)

    def test_by_label_wrong_key(self):
        with self.assertRaises(KeyError):
            Suit.by_label('herz')
