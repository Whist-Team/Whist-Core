import unittest

from whist.core.card import Rank


class RankTestCase(unittest.TestCase):
    @staticmethod
    def test_rank_order():
        assert Rank.NUM_2 < Rank.NUM_3 < Rank.NUM_4 < Rank.NUM_5 < Rank.NUM_6 < Rank.NUM_7 \
               < Rank.NUM_8 < Rank.NUM_9 < Rank.NUM_10 < Rank.J < Rank.Q < Rank.K < Rank.A

    def test_by_label(self):
        jack = Rank.by_label('jack')
        self.assertEqual(Rank.J, jack)

    def test_by_short_label(self):
        jack = Rank.by_label('J', search_short_labels=True)
        self.assertEqual(Rank.J, jack)

    def test_by_label_wrong_key(self):
        with self.assertRaises(KeyError):
            Rank.by_label('jones')
