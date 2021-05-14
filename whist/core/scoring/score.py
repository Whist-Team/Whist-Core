from typing import Any

from pydantic import BaseModel

from whist.core.player import Player


class Score(BaseModel):
    tick_score: dict = {}

    def __init__(self, players: list[Player], scores: list[int], **data: Any):
        super().__init__(**data)
        self.add_score(players, scores)

    def __getitem__(self, item):
        return self.tick_score[item]

    def __iter__(self):
        for player in self.tick_score:
            yield player

    def add_score(self, players: list[Player], scores: list[int]) -> None:
        for player, score in zip(players, scores):
            self.tick_score.update({player: score})
