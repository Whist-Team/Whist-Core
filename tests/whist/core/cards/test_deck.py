import unittest

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.deck import Deck


class DeckTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Deck()
        self.spades_king = Card(Suit.SPADES, Rank.K)

    def test_empty(self):
        self.assertEqual(Deck(), Deck.empty())

    def test_contains(self):
        deck = Deck(self.spades_king)
        self.assertIn(self.spades_king, deck)

    def test_add(self):
        self.deck.add(self.spades_king)
        self.assertIn(self.spades_king, self.deck)

    def test_full_deck_length(self):
        self.assertEqual(52, len(Deck.full()))

    def test_remove(self):
        full_deck = Deck.full()
        full_deck.remove(self.spades_king)
        self.assertNotIn(self.spades_king, full_deck)

    def test_add_duplicate(self):
        self.deck.add(self.spades_king)
        with self.assertRaises(KeyError):
            self.deck.add(self.spades_king)

    def test_iter(self):
        queen_diamonds = Card(Suit.DIAMONDS, Rank.Q)
        cards = {self.spades_king, queen_diamonds}
        deck = Deck(cards)
        self.assertSetEqual(cards, {card for card in deck})


