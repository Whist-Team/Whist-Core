import unittest
from unittest.mock import MagicMock

from whist_core.scoring.score import Score
from whist_core.scoring.score_calculator import ScoreCalculator


class TestScoreCalculator(unittest.TestCase):
    def test_single_score(self):
        player_a = MagicMock(team=0, player=MagicMock(username='a', rating=1200))
        player_b = MagicMock(team=0, player=MagicMock(username='b', rating=1200))
        player_c = MagicMock(team=1, player=MagicMock(username='c', rating=1200))
        player_d = MagicMock(team=1, player=MagicMock(username='d', rating=1200))
        play_order = MagicMock(play_order=[player_a, player_c, player_b, player_d])
        play_order.__iter__ = MagicMock(return_value=iter(play_order.play_order))
        teams = [MagicMock(players=[player_a, player_b]), MagicMock(players=[player_c, player_d])]
        tricks = []
        for _ in range(0, 6):
            trick = MagicMock(winner=player_a)
            tricks.append(trick)
        hand = MagicMock(tricks=tricks)
        expected_score = Score(scores=[1, 0], teams=teams)
        score = ScoreCalculator.calc_score(hand, play_order)
        self.assertEqual(expected_score, score)
