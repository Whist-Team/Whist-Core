"""Extraction of common methods for card containers."""
from typing import Iterable, Iterator, Any

from whist.core.cards.card import Card


class CardContainer:
    """
    Super class for class that contains a set of cards.
    """

    def __init__(self, *args: (tuple[Iterable[Card]], tuple[Card, ...])) -> None:
        """
        Constructor

        :param args: multiple cards or one card iterable
        """
        if len(args) == 1 and not isinstance(args[0], Card):
            self._cards = {*args[0]}
        else:
            self._cards = {*args}

    def __contains__(self, card: Card) -> bool:
        return card in self._cards

    def __len__(self):
        return len(self._cards)

    def __iter__(self) -> Iterator[Card]:
        return iter(self._cards)

    def __eq__(self, other: Any) -> bool:
        if self.__class__ is other.__class__:
            # pylint: disable=protected-access
            return self._cards == other._cards
        return NotImplemented

    def __str__(self) -> str:
        return str(self._cards)

    def remove(self, card: Card) -> None:
        """
        Remove a card from this deck.

        :param card: card to remove
        """
        self._cards.remove(card)
