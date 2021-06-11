import unittest

from whist.core.cards.card import Suit, Rank, Card


class CardTestCase(unittest.TestCase):
    def setUp(self):
        self.card = Card(Suit.HEARTS, Rank.A)

    def test_card_equality(self):
        card = Card(Suit.HEARTS, Rank.A)
        self.assertEqual(card, self.card)

    def test_short_name(self):
        self.assertEqual('♥A', self.card.short_name)

    def test_name(self):
        self.assertEqual('ace of hearts', self.card.name)

    def test_str(self):
        self.assertEqual('ace of hearts', str(self.card))
