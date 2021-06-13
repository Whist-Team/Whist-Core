import collections

from whist.core.cards.card import Suit
from whist.core.cards.deck import Deck
from whist.core.game.player_at_table import PlayerAtTable
from whist.core.game.trick import Trick
from whist.core.game.warnings import TrickNotDoneWarning


class Hand:
    def __init__(self, play_order: list[PlayerAtTable], trump: Suit):
        self._tricks: list[Trick] = []
        self._current_play_order: list[PlayerAtTable] = play_order
        self._trump = trump

    def deal(self) -> Trick:
        deck = Deck.full()
        trump = None
        while len(deck) > 0:
            for player in self._current_play_order:
                card = deck.pop_random()
                if len(deck) == 1:
                    trump = card.suit
                player.hand.add(card)
        if trump is None:
            raise ValueError
        first_trick = Trick(self._current_play_order, trump)
        self._tricks.append(first_trick)
        return first_trick

    def next_trick(self) -> Trick:
        if not self._tricks[-1].done:
            raise TrickNotDoneWarning()
        self._winner_plays_first_card()
        next_trick = Trick(self._current_play_order, trump=self._trump)
        self._tricks.append(next_trick)
        return next_trick

    def _winner_plays_first_card(self):
        winner: PlayerAtTable = self._tricks[-1].winner
        deque = collections.deque(self._current_play_order)
        rotation: int = self._current_play_order.index(winner)
        deque.rotate(rotation)
        self._current_play_order = list(deque)
