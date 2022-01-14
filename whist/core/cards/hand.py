"""Hand held by player."""

from whist.core.cards.card import Suit
from whist.core.cards.card_container import CardContainer


class Hand(CardContainer):
    """
    Hand of player during a game.
    """

    def contains_suit(self, suit: Suit) -> bool:
        """
        Checks if a card of a suit is still in the hand.

        :param suit: which should be checked
        :type suit: Suit
        :return: True if contains this suit else False
        :rtype: bool
        """
        if len(self) == 0:
            return False
        return any((card for card in self if card.suit == suit))
