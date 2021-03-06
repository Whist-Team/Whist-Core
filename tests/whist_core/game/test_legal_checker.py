from unittest import TestCase

from whist_core.cards.card import Card, Suit, Rank
from whist_core.cards.card_container import UnorderedCardContainer
from whist_core.game.legal_checker import LegalChecker


class TestLegalCheckerCase(TestCase):
    def test_first_card(self):
        hand = UnorderedCardContainer.empty()
        first_card = Card(suit=Suit.CLUBS, rank=Rank.A)
        second_card = Card(suit=Suit.CLUBS, rank=Rank.K)
        hand.add(second_card)

        self.assertTrue(LegalChecker.check_legal(hand, first_card, None))

    def test_suit_served(self):
        hand = UnorderedCardContainer.empty()
        first_card = Card(suit=Suit.CLUBS, rank=Rank.A)
        second_card = Card(suit=Suit.CLUBS, rank=Rank.K)
        third_card = Card(suit=Suit.CLUBS, rank=Rank.Q)
        hand.add(second_card)

        self.assertTrue(LegalChecker.check_legal(hand, third_card, first_card))

    def test_suit_not_served(self):
        hand = UnorderedCardContainer.empty()
        first_card = Card(suit=Suit.CLUBS, rank=Rank.A)
        second_card = Card(suit=Suit.CLUBS, rank=Rank.K)
        third_card = Card(suit=Suit.HEARTS, rank=Rank.Q)
        hand.add(second_card)

        self.assertFalse(LegalChecker.check_legal(hand, third_card, first_card))
