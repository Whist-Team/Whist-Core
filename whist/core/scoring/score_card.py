from whist.core.player import Player
from whist.core.scoring.score import Score


class ScoreCard:
    ticks: list['Score'] = []

    def __len__(self):
        return len(self.ticks)

    def add_score(self, score: Score):
        self.ticks.append(score)

    def num_against_opp(self, player: Player, opponent: Player) -> int:
        tick: dict
        return len([tick for tick in self.ticks if player in tick and opponent in tick])

    def score_against_opp(self, player: Player, opponent: Player) -> int:
        pass
