"""
Result after one hand.
"""
from typing import Any

from pydantic import BaseModel

from whist.core.player import Player


class Score(BaseModel):
    """
    Score of a hand being played.
    """
    tick_score: dict = {}

    def __init__(self, players: list[Player], scores: list[int], **data: Any):
        super().__init__(**data)
        for player, score in zip(players, scores):
            self.tick_score.update({player: score})

    def __getitem__(self, item):
        return self.tick_score[item]

    def __iter__(self):
        for player in self.tick_score:
            yield player
