from typing import Iterable, final, Iterator, Any, NoReturn

from whist.card import Card, Suit, Rank


@final
class Deck:
    """An unordered collection of cards"""
    __cards: set[Card]

    def __init__(self, *args: (tuple[Iterable[Card]], tuple[Card, ...])) -> NoReturn:
        """
        Constructor

        :param args: multiple cards or one card iterable
        """
        if len(args) == 1 and not isinstance(args[0], Card):
            self.__cards = {*args[0]}
        else:
            self.__cards = {*args}

    def add(self, card: Card) -> NoReturn:
        """
        Add a card to this deck.

        :param card: card to add
        """
        if card in self.__cards:
            raise KeyError
        self.__cards.add(card)

    def remove(self, card: Card) -> NoReturn:
        """
        Remove a card from this deck.

        :param card: card to remove
        """
        self.__cards.remove(card)

    def __contains__(self, item: Any) -> bool:
        return item in self.__cards

    def __len__(self):
        return len(self.__cards)

    def __iter__(self) -> Iterator[Card]:
        return iter(self.__cards)

    def __str__(self) -> str:
        return str(self.__cards)

    def __repr__(self) -> str:
        return f'Deck(cards={self.__cards!r})'

    def __eq__(self, other: Any) -> bool:
        if self.__class__ is other.__class__:
            return self.__cards == other.__cards
        return NotImplemented

    def __ne__(self, other: Any) -> bool:
        if self.__class__ is other.__class__:
            return self.__cards != other.__cards
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__cards)

    @staticmethod
    def empty():
        """
        Create an empty deck.

        :return: empty deck
        """
        return Deck()

    @staticmethod
    def full():
        """
        Create a full deck.

        :return: full deck
        """
        return Deck((Card(suit, rank) for suit in Suit for rank in Rank))