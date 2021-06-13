"""One Game of whist"""
from pydantic import BaseModel

from whist.core.scoring.score_card import ScoreCard
from whist.core.scoring.team import Team


class Game(BaseModel):
    """
    One Game of whist.
    """
    teams: list[Team] = []
    win_score: int = 3
    score_card: ScoreCard = ScoreCard()

    @property
    def done(self):
        """
        Check if game is done.
        :return: True if done else false
        :rtype: bool
        """
        return self.win_score <= max(self.score_card)
