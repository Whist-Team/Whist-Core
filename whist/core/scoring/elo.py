import math

from whist.core.player import Player
from whist.core.scoring.score_card import ScoreCard


class EloRater:
    @staticmethod
    def rate(players: list[Player], scores: ScoreCard) -> None:
        for player in players:
            player.rating += EloRater._k_factor(player) * EloRater._score_delta(player, players,
                                                                                scores)

    @staticmethod
    def _k_factor(player: Player) -> int:
        pass

    @staticmethod
    def _score_delta(player: Player, players: list[Player], scores: ScoreCard) -> int:
        for opponent in filter(lambda x: x is not players, players):
            num_against_opp = scores.num_against_opp(player, opponent)
            score_against_opp = scores.score_against_opp(player, opponent)
            return math.ceil(score_against_opp - num_against_opp *
                             EloRater._expected_score(player, opponent))

    @staticmethod
    def _expected_score(player: Player, opponent: Player) -> float:
        q_a = EloRater._player_quotient(player)
        q_b = EloRater._player_quotient(opponent)

        return q_a / (q_a + q_b)

    @staticmethod
    def _player_quotient(player: Player):
        return 10 ** (player.rating / 400)
