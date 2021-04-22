import unittest

from whist.card import Suit, Rank, Card


class CardTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.card = Card(Suit.HEARTS, Rank.A)

    def test_suit_order(self):
        self.assertLess(Suit.CLUBS, Suit.DIAMONDS)
        self.assertLess(Suit.DIAMONDS, Suit.HEARTS)
        self.assertLess(Suit.HEARTS, Suit.SPADES)

    def test_rank_order(self):
        assert Rank.NUM_2 < Rank.NUM_3 < Rank.NUM_4 < Rank.NUM_5 < Rank.NUM_6 < Rank.NUM_7 \
               < Rank.NUM_8 < Rank.NUM_9 < Rank.NUM_10 < Rank.J < Rank.Q < Rank.K < Rank.A

    def test_card_equality(self):
        card = Card(Suit.HEARTS, Rank.A)
        self.assertEqual(card, self.card)

    def test_short_name(self):
        self.assertEqual('♥A', self.card.short_name)

    def test_name(self):
        self.assertEqual('ace of hearts', self.card.name)
