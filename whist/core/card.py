from dataclasses import dataclass
from enum import Enum, unique


class OrderedEnum(Enum):
    _ordinal: int

    def __new__(cls, *args):
        if len(args) == 1:
            value = args[0]
        else:
            value = args

        obj = object.__new__(cls)
        obj._value_ = value
        obj._ordinal = len(cls.__members__)
        return obj

    @classmethod
    def by_ordinal(cls, ordinal: int):
        return cls[ordinal]

    @property
    def ordinal(self) -> int:
        return self._ordinal

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.ordinal >= other.ordinal
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.ordinal > other.ordinal
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.ordinal <= other.ordinal
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.ordinal < other.ordinal
        return NotImplemented


@unique
class Suit(OrderedEnum):
    CLUBS = ('♣', 'clubs')
    DIAMONDS = ('♦', 'diamonds')
    HEARTS = ('♥', 'hearts')
    SPADES = ('♠', 'spades')

    @classmethod
    def by_label(cls, label: str, search_short_labels: bool = False):
        for name, value in cls.__members__.items():
            if value.label == label:
                return value
            elif search_short_labels and value.short_label == label:
                return value
        raise KeyError

    @property
    def short_label(self) -> str:
        return self.value if type(self.value) is str else self.value[0]

    @property
    def label(self) -> str:
        return self.value if type(self.value) is str else self.value[1]

    def __str__(self) -> str:
        return self.label


@unique
class Rank(OrderedEnum):
    NUM_2 = '2'
    NUM_3 = '3'
    NUM_4 = '4'
    NUM_5 = '5'
    NUM_6 = '6'
    NUM_7 = '7'
    NUM_8 = '8'
    NUM_9 = '9'
    NUM_10 = '10'
    J = ('J', 'jack')
    Q = ('Q', 'queen')
    K = ('K', 'king')
    A = ('A', 'ace')

    @classmethod
    def by_label(cls, label: str, search_short_labels: bool = False):
        for name, value in cls.__members__.items():
            if value.label == label:
                return value
            elif search_short_labels and value.short_label == label:
                return value
        raise KeyError

    @property
    def short_label(self) -> str:
        return self.value if type(self.value) is str else self.value[0]

    @property
    def label(self) -> str:
        return self.value if type(self.value) is str else self.value[1]

    def __str__(self) -> str:
        return self.label


@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: Rank

    @property
    def short_name(self) -> str:
        return f'{self.suit.short_label}{self.rank.short_label}'

    @property
    def name(self) -> str:
        return f'{self.rank} of {self.suit}'

    def __str__(self) -> str:
        return self.name
