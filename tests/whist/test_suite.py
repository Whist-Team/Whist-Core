import unittest

from whist.card import Rank, Suit


class SuitTestCase(unittest.TestCase):
    def test_by_label(self):
        clubs = Suit.by_label('clubs')
        self.assertEqual(Suit.CLUBS, clubs)

    def test_by_label_wrong_key(self):
        with self.assertRaises(KeyError):
            Rank.by_label('herz')
