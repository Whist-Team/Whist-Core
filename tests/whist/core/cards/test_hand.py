import unittest

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.hand import Hand


class HandTestCase(unittest.TestCase):
    def contains_suit(self):
        hand = Hand()
        hand.add(Card(Suit.HEARTS, Rank.NUM_8))
        self.assertTrue(hand.contain_suit(Suit.HEARTS))

    def contains_not_suit(self):
        hand = Hand()
        hand.add(Card(Suit.CLUBS, Rank.NUM_8))
        self.assertTrue(hand.contain_suit(Suit.HEARTS))
