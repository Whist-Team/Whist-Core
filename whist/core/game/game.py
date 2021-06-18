"""One Game of whist"""
from typing import Optional

from whist.core.game.hand import Hand
from whist.core.scoring.score_card import ScoreCard
from whist.core.scoring.team import Team


class Game:
    """
    One Game of whist.
    """

    def __init__(self, teams=None):
        super().__init__()
        if teams is None:
            teams = []
        self.teams: list[Team] = teams
        self.win_score: int = 3
        self.score_card: ScoreCard = ScoreCard()
        self._current_hand: Optional[Hand] = None

    def next_hand(self) -> Hand:
        if self._current_hand is None:
            play_order = [None] * 4
            for team_index, team in enumerate(self.teams):
                for player_index, player in enumerate(team.players):
                    play_order[team_index + player_index * len(self.teams)] = player
            self._current_hand = Hand(play_order)
        return self._current_hand

    @property
    def done(self):
        """
        Check if game is done.
        :return: True if done else false
        :rtype: bool
        """
        return self.win_score <= self.score_card.max
