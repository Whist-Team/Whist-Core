import unittest

from whist.core.player import Player
from whist.core.scoring.elo import EloRater
from whist.core.scoring.score import Score
from whist.core.scoring.score_card import ScoreCard


class EloRaterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.player_a = Player(user_id=2, username='a', rating=1600)
        self.player_b = Player(user_id=3, username='b', rating=1800)

    def test_rate_one_game(self):
        score_card = ScoreCard()
        score = Score([self.player_a, self.player_b], [7, 6])
        score_card.add_score(score)
        EloRater.rate([self.player_a, self.player_b], score_card)
        self.assertEqual(1630, self.player_a.rating)
        self.assertEqual(1770, self.player_b.rating)

    def test_rate_multiple_games(self):
        score_card = ScoreCard()
        score = Score([self.player_a, self.player_b], [7, 6])
        score_card.add_score(score)
        score_card.add_score(score)
        score = Score([self.player_a, self.player_b], [6, 7])
        score_card.add_score(score)

        EloRater.rate([self.player_a, self.player_b], score_card)

        self.assertLess(1600, self.player_a.rating)
        self.assertGreater(1800, self.player_b.rating)
