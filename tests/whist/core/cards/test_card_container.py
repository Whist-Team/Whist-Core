import json
from unittest import TestCase

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.card_container import CardContainer


class CardContainerTestCase(TestCase):
    def setUp(self) -> None:
        self.spades_king = Card(suit=Suit.SPADES, rank=Rank.K)

    def test_not_equal(self):
        first = CardContainer.with_cards(Card(suit=Suit.HEARTS, rank=Rank.NUM_2))
        second = CardContainer.with_cards(Card(suit=Suit.HEARTS, rank=Rank.NUM_4))
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

    def test_pop_random(self):
        full_cc = CardContainer.full()
        popped_card = full_cc.pop_random()
        self.assertIsInstance(popped_card, Card)
        self.assertNotIn(popped_card, full_cc)

    def test_json(self):
        cc = CardContainer.with_cards(
            Card(suit=Suit.HEARTS, rank=Rank.NUM_2),
            Card(suit=Suit.HEARTS, rank=Rank.NUM_4)
        )
        self.assertEqual({'cards': [
            {'suit': 'hearts', 'rank': '2'},
            {'suit': 'hearts', 'rank': '4'}
        ]}, json.loads(cc.json()))

    def test_contains(self):
        cc = CardContainer.with_cards(self.spades_king)
        self.assertEqual(1, len(cc))
        self.assertIn(self.spades_king, cc)

    def test_add(self):
        cc = CardContainer.empty()
        cc.add(self.spades_king)
        self.assertEqual(1, len(cc))
        self.assertIn(self.spades_king, cc)

    def test_add_duplicate(self):
        cc = CardContainer.empty()
        cc.add(self.spades_king)
        with self.assertRaises(ValueError):
            cc.add(self.spades_king)

    def test_add_none(self):
        cc = CardContainer.empty()
        with self.assertRaises(ValueError):
            cc.add(None)

    def test_add_wrong_type(self):
        cc = CardContainer.empty()
        with self.assertRaises(ValueError):
            cc.add('ace of spades')

    def test_remove(self):
        cc = CardContainer.full()
        cc.remove(self.spades_king)
        self.assertNotIn(self.spades_king, cc)

    def test_remove_no_contain(self):
        cc = CardContainer.empty()
        with self.assertRaises(ValueError):
            cc.remove(self.spades_king)

    def test_remove_none(self):
        cc = CardContainer.full()
        with self.assertRaises(ValueError):
            cc.remove(None)

    def test_remove_wrong_type(self):
        cc = CardContainer.full()
        with self.assertRaises(ValueError):
            cc.remove('ace of spades')

    def test_iter(self):
        queen_diamonds = Card(suit=Suit.DIAMONDS, rank=Rank.Q)
        cards = {self.spades_king, queen_diamonds}
        cc = CardContainer.with_cards(cards)
        self.assertEqual(cards, {card for card in cc})
