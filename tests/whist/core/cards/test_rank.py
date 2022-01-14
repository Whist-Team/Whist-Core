import unittest

from whist.core.cards.card import Rank


class RankTestCase(unittest.TestCase):
    @staticmethod
    def test_rank_order():
        assert Rank.NUM_2 < Rank.NUM_3 < Rank.NUM_4 < Rank.NUM_5 < Rank.NUM_6 < Rank.NUM_7 \
               < Rank.NUM_8 < Rank.NUM_9 < Rank.NUM_10 < Rank.J < Rank.Q < Rank.K < Rank.A

    def test_by_name(self):
        jack = Rank('jack')
        self.assertEqual(Rank.J, jack)

    def test_by_short_name(self):
        jack = Rank('J')
        self.assertEqual(Rank.J, jack)

    def test_constructor_lookup_wrong_key(self):
        with self.assertRaises(ValueError):
            Rank('jones')

    def test_by_name_wrong_key(self):
        with self.assertRaises(ValueError):
            Rank('jones')
