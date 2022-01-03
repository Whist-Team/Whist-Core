import unittest

from whist.core.cards.card import Card, Rank, Suit
from whist.core.cards.stack import Stack


class StackTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.king_hearts = Card(Suit.HEARTS, Rank.K)
        cls.ace_hearts = Card(Suit.HEARTS, Rank.A)
        cls.seven_club = Card(Suit.CLUBS, Rank.NUM_7)
        cls.ten_diamond = Card(Suit.DIAMONDS, Rank.NUM_10)
        cls.stack = Stack()
        cls.stack.add(cls.king_hearts)
        cls.stack.add(cls.seven_club)
        cls.stack.add(cls.ten_diamond)
        cls.stack.add(cls.ace_hearts)

    def test_winner_suit(self):
        self.assertEqual(self.ace_hearts, self.stack.winner_card(Suit.SPADES))

    def test_winner_trump(self):
        self.assertEqual(self.seven_club, self.stack.winner_card(Suit.CLUBS))

    def test_len(self):
        self.assertEqual(4, len(self.stack))

    def test_index(self):
        for index, card in enumerate([self.king_hearts, self.seven_club, self.ten_diamond,
                                      self.ace_hearts]):
            turn = self.stack.get_turn(card)
            self.assertEqual(index, turn, msg=f'Turn should be {index}, but was {turn}.')

    def test_double_add(self):
        with self.assertRaises(KeyError):
            self.stack.add(self.seven_club)

    def test_turn_card_not_in(self):
        with self.assertRaises(KeyError):
            self.stack.get_turn(Card(Suit.CLUBS, Rank.NUM_8))

    def test_equal(self):
        first_stack = Stack()
        second_stack = Stack()
        first_stack.add(self.seven_club)
        second_stack.add(self.seven_club)
        self.assertEqual(first_stack, second_stack)

    def test_not_equal(self):
        first_stack = Stack()
        second_stack = Stack()
        first_stack.add(self.seven_club)
        self.assertNotEqual(first_stack, second_stack)

    def test_not_instance(self):
        with self.assertRaises(ValueError):
            Stack() == object()
