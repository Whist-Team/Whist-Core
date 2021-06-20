from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.scoring.elo import EloRater
from whist.core.scoring.score import Score
from whist.core.scoring.score_card import ScoreCard


class EloRaterTestCase(TeamBaseTestCase):

    def test_rate_one_game(self):
        score_card = ScoreCard()
        score = Score([self.team_a, self.team_b], [7, 6])
        score_card.add_score(score)
        EloRater.rate([self.team_a, self.team_b], score_card)
        self.assertEqual(1620, self.team_a.players[0].rating)
        self.assertEqual(1820, self.team_a.players[1].rating)
        self.assertEqual(1680, self.team_b.players[0].rating)
        self.assertEqual(1680, self.team_b.players[1].rating)

    def test_rate_multiple_games(self):
        score_card = ScoreCard()
        score = Score([self.team_a, self.team_b], [7, 6])
        score_card.add_score(score)
        score_card.add_score(score)
        score = Score([self.team_a, self.team_b], [6, 7])
        score_card.add_score(score)

        EloRater.rate([self.team_a, self.team_b], score_card)

        self.assertLess(1600, self.team_a.players[0].rating)
        self.assertLess(1800, self.team_a.players[1].rating)
        self.assertGreater(1700, self.team_b.players[0].rating)
        self.assertGreater(1700, self.team_b.players[1].rating)
