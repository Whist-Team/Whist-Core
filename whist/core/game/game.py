"""One Game of whist"""
from pydantic import BaseModel

from whist.core.scoring.score_card import ScoreCard
from whist.core.scoring.team import Team


class Game(BaseModel):
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

    @property
    def done(self):
        """
        Check if game is done.
        :return: True if done else false
        :rtype: bool
        """
        return self.win_score <= max(self.score_card)
