import unittest

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.hand import Hand


class HandTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.hand = Hand()
        self.spades_king = Card(Suit.SPADES, Rank.K)

    def contains_suit(self):
        hand = Hand()
        hand.add(Card(Suit.HEARTS, Rank.NUM_8))
        self.assertTrue(hand.contain_suit(Suit.HEARTS))

    def contains_not_suit(self):
        hand = Hand()
        hand.add(Card(Suit.CLUBS, Rank.NUM_8))
        self.assertTrue(hand.contain_suit(Suit.HEARTS))

    def test_empty(self):
        self.assertEqual(Hand(), Hand.empty())

    def test_contains(self):
        hand = Hand(self.spades_king)
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
        with self.assertRaises(KeyError):
            self.hand.add(self.spades_king)

    def test_iter(self):
        queen_diamonds = Card(Suit.DIAMONDS, Rank.Q)
        cards = {self.spades_king, queen_diamonds}
        hand = Hand(cards)
        self.assertSetEqual(cards, {card for card in hand})

    def test_contain_suit(self):
        self.hand.add(self.spades_king)
        self.assertTrue(self.hand.contain_suit(Suit.SPADES))

    def test_not_contain_suit(self):
        self.assertFalse(self.hand.contain_suit(Suit.SPADES))
        self.assertFalse(self.hand.contain_suit(Suit.HEARTS))
        self.assertFalse(self.hand.contain_suit(Suit.CLUBS))
        self.assertFalse(self.hand.contain_suit(Suit.DIAMONDS))
