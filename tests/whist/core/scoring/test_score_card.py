import unittest

from whist.core.player import Player
from whist.core.scoring.score import Score
from whist.core.scoring.score_card import ScoreCard


class ScoreCardTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.score_card = ScoreCard()
        self.player_a = Player(user_id=2, username='a', rating=1200)
        self.player_b = Player(user_id=3, username='b', rating=1400)

    def test_add_score(self):
        score = Score([self.player_a, self.player_b], [7, 6])
        self.score_card.add_score(score)
        self.assertEqual(1, len(self.score_card))

    def test_num_against_opp(self):
        assert False
