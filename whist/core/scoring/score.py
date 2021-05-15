"""
Result after one hand.
"""
from typing import Any

from pydantic import BaseModel

from whist.core.scoring.team import Team


class Score(BaseModel):
    """
    Score of a hand being played.
    """
    hand_score: dict = {}

    def __init__(self, teams: list[Team], scores: list[int], **data: Any):
        super().__init__(**data)
        for team, score in zip(teams, scores):
            self.hand_score.update({team: score})
            team.games_played()

    def __getitem__(self, item):
        return self.hand_score[item]

    def __iter__(self):
        for team in self.hand_score:
            yield team

    def won_against(self, team: Team, opponent: Team):
        return self.hand_score[team] > self.hand_score[opponent]
