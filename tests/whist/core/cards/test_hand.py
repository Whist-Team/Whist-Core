import unittest

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.hand import Hand


class HandTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.hand = Hand.empty()
        self.spades_king = Card(suit=Suit.SPADES, rank=Rank.K)

    def contains_suit(self):
        hand = Hand.empty()
        hand.add(Card(suit=Suit.HEARTS, rank=Rank.NUM_8))
        self.assertTrue(hand.contains_suit(Suit.HEARTS))

    def contains_not_suit(self):
        hand = Hand.empty()
        hand.add(Card(suit=Suit.CLUBS, rank=Rank.NUM_8))
        self.assertTrue(hand.contains_suit(Suit.HEARTS))

    def test_empty(self):
        self.assertEqual(Hand(cards=()), Hand.empty())

    def test_contains(self):
        hand = Hand.with_cards(self.spades_king)
        self.assertIn(self.spades_king, hand)

    def test_add(self):
        self.hand.add(self.spades_king)
        self.assertIn(self.spades_king, self.hand)

    def test_remove(self):
        self.hand.add(self.spades_king)
        self.hand.remove(self.spades_king)
        self.assertNotIn(self.spades_king, self.hand)

    def test_add_duplicate(self):
        self.hand.add(self.spades_king)
        with self.assertRaises(ValueError):
            self.hand.add(self.spades_king)

    def test_iter(self):
        queen_diamonds = Card(suit=Suit.DIAMONDS, rank=Rank.Q)
        cards = {self.spades_king, queen_diamonds}
        hand = Hand.with_cards(cards)
        self.assertSetEqual(cards, {card for card in hand})

    def test_contain_suit(self):
        self.hand.add(self.spades_king)
        self.assertTrue(self.hand.contains_suit(Suit.SPADES))

    def test_not_contain_suit(self):
        self.assertFalse(self.hand.contains_suit(Suit.SPADES))
        self.assertFalse(self.hand.contains_suit(Suit.HEARTS))
        self.assertFalse(self.hand.contains_suit(Suit.CLUBS))
        self.assertFalse(self.hand.contains_suit(Suit.DIAMONDS))
