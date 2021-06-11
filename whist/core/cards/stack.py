"""Collection of cards"""
from whist.core.cards.card import Card, Suit


class Stack:
    """An ordered collection of cards"""
    __cards: list[Card] = []

    def __len__(self):
        return len(self.__cards)

    def add(self, card: Card) -> None:
        """
        Put card on top of stack
        :param card: a Card placed on top of the stack
        """
        self.__cards.append(card)

    def winner_card(self, trump: Suit) -> Card:
        """
        Returns the highest trump card or the highest card of the suit played first.
        :param trump: suit of trump
        :type trump: Suit
        :return: the winning card
        :rtype: Card
        """
        winner_suit_cards: list[Card] = self._card_of_suit(trump)
        if len(winner_suit_cards) == 0:
            winner_suit_cards: list[Card] = self._card_of_suit(self.__cards[0].suit)
        return max(winner_suit_cards, key=lambda x: x.rank)

    def _card_of_suit(self, trump):
        return [card for card in self.__cards if card.suit == trump]
