"""Scoring util"""
from whist_core.game.hand import Hand
from whist_core.game.play_order import PlayOrder
from whist_core.scoring.score import Score
from whist_core.scoring.team import Team

# A team score for each trick exceeding 6.
TRICK_EXCESS_BASE = 6


# pylint: disable=too-few-public-methods
class ScoreCalculator:
    """
    Util class for score calculating.
    """

    @staticmethod
    def calc_score(hand: Hand, play_order: PlayOrder) -> Score:
        """
        Calculates the score at the end of the hand.
        :param hand: the hand to be scored
        :param play_order: the order of players
        :return: Score
        """
        tricks_won = ScoreCalculator.count_wins(hand)
        players_by_team = play_order.to_team_list()
        teams = [Team(players=players) for players in players_by_team]
        score = Score(teams=teams, scores=tricks_won)
        return score

    @staticmethod
    def count_wins(hand: Hand) -> list[int]:
        tricks_won = [0, 0]
        for trick in hand.tricks:
            winner = trick.winner
            tricks_won[winner.team] += 1
        return [max(0, trick_score - TRICK_EXCESS_BASE) for trick_score in tricks_won]
