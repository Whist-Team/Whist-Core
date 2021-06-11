import unittest

from whist.core.cards.card import Card, Rank, Suit
from whist.core.cards.stack import Stack


class StackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.king_hearts = Card(Suit.HEARTS, Rank.K)
        self.ace_hearts = Card(Suit.HEARTS, Rank.A)
        self.seven_club = Card(Suit.CLUBS, Rank.NUM_7)
        self.ten_diamond = Card(Suit.DIAMONDS, Rank.NUM_10)
        self.stack = Stack()
        self.stack.add(self.king_hearts)
        self.stack.add(self.seven_club)
        self.stack.add(self.ten_diamond)
        self.stack.add(self.ace_hearts)

    def test_winner_suit(self):
        self.assertEqual(self.ace_hearts, self.stack.winner_card(Suit.SPADES))
