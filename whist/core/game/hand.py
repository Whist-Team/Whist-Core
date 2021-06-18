"""Hand of whist"""
import collections
from typing import Union

from whist.core.cards import hand
from whist.core.cards.deck import Deck
from whist.core.game.player_at_table import PlayerAtTable
from whist.core.game.trick import Trick
from whist.core.game.warnings import TrickNotDoneWarning
from whist.core.user.player import Player


class Hand:
    """
    Hand of whist.
    """

    def __init__(self, play_order: list[Union[Player, PlayerAtTable]]):
        self._tricks: list[Trick] = []
        for index, player in enumerate(play_order):
            if isinstance(player, Player):
                play_order[index] = PlayerAtTable(player, hand.Hand.empty())
        self._current_play_order: list[PlayerAtTable] = play_order
        self._trump = None

    def deal(self) -> Trick:
        """
        Deals the hand and starts the first trick.
        :return: the first trick
        :rtype: Trick
        """
        deck = Deck.full()
        while len(deck) > 0:
            for player in self._current_play_order:
                card = deck.pop_random()
                if len(deck) == 1:
                    self._trump = card.suit
                player.hand.add(card)
        if self._trump is None:
            raise ValueError
        first_trick = Trick(self._current_play_order, self._trump)
        self._tricks.append(first_trick)
        return first_trick

    def next_trick(self) -> Trick:
        """
        Starts the next trick.
        :return: the next trick
        :rtype: Trick
        """
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
