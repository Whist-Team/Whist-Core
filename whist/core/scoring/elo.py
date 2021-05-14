from copy import deepcopy

from whist.core.player import Player
from whist.core.scoring.score_card import ScoreCard


class EloRater:
    @staticmethod
    def rate(players: list[Player], scores: ScoreCard) -> None:
        original_players = deepcopy(players)
        for player, original_player in zip(players, original_players):
            k_factor = EloRater._k_factor(original_player)
            delta = EloRater._score_delta(original_player, original_players, scores)
            player.rating += round(k_factor * delta)

    @staticmethod
    def _k_factor(player: Player) -> int:
        if player.rating > 2400 and player.games > 30:
            return 10
        if player.rating < 2300 and player.games < 30:
            return 40
        return 20

    @staticmethod
    def _score_delta(player: Player, players: list[Player], scores: ScoreCard) -> float:
        for opponent in filter(lambda x: x is not player, players):
            num_against_opp = scores.num_against_opp(player, opponent)
            score_against_opp = scores.score_against_opp(player, opponent)
            expected_score = EloRater._expected_score(player, opponent)
            return score_against_opp - num_against_opp * expected_score

    @staticmethod
    def _expected_score(player: Player, opponent: Player) -> float:
        q_a = EloRater._player_quotient(player)
        q_b = EloRater._player_quotient(opponent)

        return q_a / (q_a + q_b)

    @staticmethod
    def _player_quotient(player: Player):
        return 10 ** (player.rating / 400)
