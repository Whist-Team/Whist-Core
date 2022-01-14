import unittest

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.deck import Deck


class DeckTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Deck.empty()
        self.spades_king = Card(suit=Suit.SPADES, rank=Rank.K)

    def test_empty(self):
        self.assertEqual(Deck(cards=()), Deck.empty())

    def test_contains(self):
        deck = Deck.with_cards(self.spades_king)
        self.assertEqual(1, len(deck))
        self.assertIn(self.spades_king, deck)

    def test_add(self):
        self.deck.add(self.spades_king)
        self.assertIn(self.spades_king, self.deck)

    def test_remove(self):
        full_deck = Deck.full()
        full_deck.remove(self.spades_king)
        self.assertNotIn(self.spades_king, full_deck)

    def test_add_duplicate(self):
        self.deck.add(self.spades_king)
        with self.assertRaises(ValueError):
            self.deck.add(self.spades_king)

    def test_iter(self):
        queen_diamonds = Card(suit=Suit.DIAMONDS, rank=Rank.Q)
        cards = {self.spades_king, queen_diamonds}
        deck = Deck.with_cards(cards)
        self.assertSetEqual(cards, {card for card in deck})
