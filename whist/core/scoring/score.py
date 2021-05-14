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
    hand_score: dict = {}

    def __init__(self, players: list[Player], scores: list[int], **data: Any):
        super().__init__(**data)
        for player, score in zip(players, scores):
            self.hand_score.update({player: score})
            player.games += 1

    def __getitem__(self, item):
        return self.hand_score[item]

    def __iter__(self):
        for player in self.hand_score:
            yield player

    def played_together(self, player: Player, opponent: Player):
        return player in self.hand_score and opponent in self.hand_score

    def won_against(self, player: Player, opponent: Player):
        together = self.played_together(player, opponent)
        won = self.hand_score[player] > self.hand_score[opponent]
        return together and won
