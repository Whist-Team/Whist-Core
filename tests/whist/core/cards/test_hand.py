import unittest

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.hand import Hand


class HandTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.spades_king = Card(suit=Suit.SPADES, rank=Rank.K)
        self.hand_with_spades_king = Hand.with_cards(self.spades_king)

    def test_contain_suit(self):
        self.assertTrue(self.hand_with_spades_king.contains_suit(Suit.SPADES))

    def test_not_contain_suit(self):
        self.assertFalse(self.hand_with_spades_king.contains_suit(Suit.HEARTS))
        self.assertFalse(self.hand_with_spades_king.contains_suit(Suit.CLUBS))
        self.assertFalse(self.hand_with_spades_king.contains_suit(Suit.DIAMONDS))
