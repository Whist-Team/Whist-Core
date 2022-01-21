"""One Game of whist"""
from typing import Optional

from whist.core.game.hand import Hand
from whist.core.game.play_order import PlayOrder
from whist.core.game.player_at_table import PlayerAtTable
from whist.core.scoring.score_card import ScoreCard
from whist.core.scoring.team import Team
from whist.core.user.player import Player


class Game:
    """
    One Game of whist.
    """

    def __init__(self, teams: list[Team]):
        super().__init__()
        self.play_order: PlayOrder = PlayOrder(teams)
        self.win_score: int = 3
        self.score_card: ScoreCard = ScoreCard()
        self.current_hand: Optional[Hand] = None

    def next_hand(self) -> Hand:
        """
        Checks if the current hand is done and if so will return the next hand. If not it will
        return the current hand.
        :rtype: Hand
        """
        if self.current_hand is None:
            self.current_hand = Hand()
        elif self.current_hand.done:
            self._next_play_order()
            self.current_hand = Hand()
        return self.current_hand

    @property
    def current_trick(self):
        """
        Returns the current trick of the current hand.
        """
        try:
            return self.next_hand().current_trick
        except IndexError:
            return self.next_hand().deal(self.play_order)

    @property
    def done(self):
        """
        Check if game is done.
        :return: True if done else false
        :rtype: bool
        """
        return self.win_score <= self.score_card.max

    def get_player(self, player: Player) -> PlayerAtTable:
        """
        Retrieves the PlayerAtTable for the player given.
        :param player: who needs it's counterpart at the table
        :return: the player at table
        """
        return self.play_order.get_player(player)

    def _next_play_order(self) -> None:
        """
        Creates the next order of player for next hand.
        """
        self.play_order = self.play_order.next_order()
