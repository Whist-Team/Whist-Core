import json
import unittest

from whist.core.cards.card import Suit, Rank, Card


class CardTestCase(unittest.TestCase):
    def setUp(self):
        self.card = Card(suit=Suit.HEARTS, rank=Rank.A)

    def test_card_equality(self):
        card = Card(suit=Suit.HEARTS, rank=Rank.A)
        self.assertEqual(card, self.card)

    def test_short_name(self):
        self.assertEqual('♥A', self.card.short_name)

    def test_name(self):
        self.assertEqual('ace of hearts', self.card.name)

    def test_str(self):
        self.assertEqual('ace of hearts', str(self.card))

    def test_dict(self):
        self.assertEqual({'suit': Suit.HEARTS, 'rank': Rank.A}, self.card.dict())

    def test_json(self):
        self.assertEqual({'suit': 'hearts', 'rank': 'ace'}, json.loads(self.card.json()))

    def test_constructor_with_enum_as_str(self):
        self.assertEqual(self.card, Card(suit='hearts', rank='ace'))

    def test_hashable(self):
        d = {self.card: 42}
        self.assertEqual(42, d[self.card])
