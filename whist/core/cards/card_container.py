"""Extraction of common methods for class that contains a set of cards"""
import random
from typing import Iterator

from pydantic import BaseModel, PrivateAttr

from whist.core.cards.card import Card


class CardContainer(BaseModel):
    """
    Super class for all classes containing unordered cards.
    """

    cards: tuple[Card, ...]
    _cards_set: set[Card] = PrivateAttr()

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Configuration class for base model to make it immutable.
        """
        allow_mutation = False

    def __init__(self, **data):
        super().__init__(**data)
        self._cards_set = set(self.cards)
        self.__resync()

    @classmethod
    def empty(cls) -> 'CardContainer':
        """
        Creates an empty card container.

        :return: empty ard container
        :rtype: correct subtype of CardContainer
        """
        return cls(cards=())

    @classmethod
    def with_cards(cls, *cards) -> 'CardContainer':
        """
        Creates a card container with the given cards.

        :param cards: cards to add
        :return: card container with given cards
        :rtype: correct subtype of CardContainer
        """
        if len(cards) == 1 and not isinstance(cards[0], Card):
            cards = cards[0]
        return cls(cards=cards)

    @classmethod
    def full(cls) -> 'CardContainer':
        """
        Create a full card container.

        :return: full card container
        :rtype: correct subtype of CardContainer
        """
        return cls(cards=Card.all_cards())

    def pop_random(self) -> Card:
        """
        Removes one random card from card container.

        :return: A card from deck.
        """
        card = random.choice(self.cards)
        self.remove(card)
        return card

    def __contains__(self, card: Card) -> bool:
        return card in self._cards_set

    def __len__(self):
        return len(self.cards)

    def __iter__(self) -> Iterator[Card]:
        return iter(self.cards)

    def __str__(self) -> str:
        return str(self.cards)

    def __repr__(self) -> str:
        return f'CardContainer(cards={self.cards!r})'

    def remove(self, card: Card) -> None:
        """
        Remove a card from this container.

        :param card: card to remove
        """
        if not isinstance(card, Card):
            raise ValueError(f'cannot remove {card} of type {type(card)} from card container')
        if card not in self._cards_set:
            raise ValueError(f'{card} not in card container')
        self._cards_set.remove(card)
        self.__resync()

    def add(self, card: Card) -> None:
        """
        Add a card to this container.

        :param card: card to add
        """
        if not isinstance(card, Card):
            raise ValueError(f'cannot add {card} of type {type(card)} to card container')
        if card in self._cards_set:
            raise ValueError(f'{card} already in card container')
        self._cards_set.add(card)
        self.__resync()

    def __resync(self):
        self.__config__.allow_mutation = True
        self.cards = tuple(sorted(self._cards_set))
        self.__config__.allow_mutation = False
