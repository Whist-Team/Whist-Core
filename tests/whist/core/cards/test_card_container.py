from unittest import TestCase

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.card_container import CardContainer


class CardContainerTestCase(TestCase):
    def test_not_equal(self):
        first = CardContainer([Card(suit=Suit.HEARTS, rank=Rank.NUM_2)])
        second = CardContainer([Card(suit=Suit.HEARTS, rank=Rank.NUM_4)])
        self.assertFalse(first == second)
