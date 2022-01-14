from unittest import TestCase

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.card_container import CardContainer


class CardContainerTestCase(TestCase):
    def test_not_equal(self):
        first = CardContainer(cards=[Card(suit=Suit.HEARTS, rank=Rank.NUM_2)])
        second = CardContainer(cards=[Card(suit=Suit.HEARTS, rank=Rank.NUM_4)])
        self.assertFalse(first == second)

    def test_empty_manual(self):
        cc = CardContainer(cards=())
        self.assertEqual(0, len(cc))

    def test_empty(self):
        cc = CardContainer.empty()
        self.assertEqual(0, len(cc))

    def test_full(self):
        cc = CardContainer.full()
        self.assertEqual(52, len(cc))

    @staticmethod
    def test_dict_no_crash():
        cc = CardContainer(cards=[Card(suit=Suit.HEARTS, rank=Rank.NUM_2)])
        cc.dict()

    def test_pop_random(self):
        full_cc = CardContainer.full()
        popped_card = full_cc.pop_random()
        self.assertIsInstance(popped_card, Card)
        self.assertNotIn(popped_card, full_cc)
