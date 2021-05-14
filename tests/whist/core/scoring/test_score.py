import unittest

from whist.core.player import Player
from whist.core.scoring.score import Score


class ScoreTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.player_a = Player(user_id=2, username='a', rating=1600)
        self.player_b = Player(user_id=3, username='b', rating=1800)

    def test_score(self):
        score = Score([self.player_a, self.player_b], [7, 6])
        self.assertTrue(score[self.player_a] > score[self.player_b])