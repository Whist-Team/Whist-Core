import unittest

from whist.card import Rank


class RankTestCase(unittest.TestCase):
    def test_by_label(self):
        jack = Rank.by_label('jack')
        self.assertEqual(Rank.J, jack)

    def test_by_short_label(self):
        jack = Rank.by_label('J', search_short_labels=True)
        self.assertEqual(Rank.J, jack)

    def test_by_label_wrong_key(self):
        with self.assertRaises(KeyError):
            Rank.by_label('jones')
