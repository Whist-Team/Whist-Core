"""Hand held by player."""
from typing import final

from whist.core.cards.card import Suit, Card
from whist.core.cards.card_container import CardContainer


@final
class Hand(CardContainer):
    """
    Hand of player during a game.
    """

    def add(self, card: Card) -> None:
        """
        Add a card to this deck.

        :param card: card to add
        """
        if card in self._cards:
            raise KeyError(f'{card} already in hand')
        self._cards.add(card)

    @staticmethod
    def empty():
        """
        Creates a empty hand.
        :return: empty hand
        :rtype: Hand
        """
        return Hand()

    def contain_suit(self, suit: Suit) -> bool:
        """
        Checks if a card of a suit is still in the hand.
        :param suit: which should be checked
        :type suit: Suit
        :return: True if contains this suit else False
        :rtype: bool
        """
        if len(self._cards) == 0:
            return False
        return any((card for card in self._cards if card.suit == suit))
