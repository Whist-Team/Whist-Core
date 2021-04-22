import unittest

from whist.card import Rank


class RankTestCase(unittest.TestCase):
    def test_by_label(self):
        jack = Rank.by_label('jack')
        self.assertEqual(Rank.J, jack)
