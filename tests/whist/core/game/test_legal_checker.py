from unittest import TestCase

from whist.core.cards.card import Card, Suit, Rank
from whist.core.cards.hand import Hand
from whist.core.game.legal_checker import LegalChecker


class TestLegalCheckerCase(TestCase):
    def test_first_card(self):
        hand = Hand()
        first_card = Card(Suit.CLUBS, Rank.A)
        second_card = Card(Suit.CLUBS, Rank.K)
        hand.add(second_card)

        self.assertTrue(LegalChecker.check_legal(hand, first_card, None))

    def test_suit_served(self):
        hand = Hand()
        first_card = Card(Suit.CLUBS, Rank.A)
        second_card = Card(Suit.CLUBS, Rank.K)
        third_card = Card(Suit.CLUBS, Rank.Q)
        hand.add(second_card)

        self.assertTrue(LegalChecker.check_legal(hand, third_card, first_card))

    def test_suit_not_served(self):
        hand = Hand()
        first_card = Card(Suit.CLUBS, Rank.A)
        second_card = Card(Suit.CLUBS, Rank.K)
        third_card = Card(Suit.HEARTS, Rank.Q)
        hand.add(second_card)

        self.assertFalse(LegalChecker.check_legal(hand, third_card, first_card))
