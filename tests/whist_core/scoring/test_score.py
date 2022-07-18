from tests.whist_core.team_base_test_case import TeamBaseTestCase
from whist_core.scoring.score import Score


class ScoreTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.score = Score([self.team_a, self.team_b], [7, 6])

    def test_score(self):
        self.assertTrue(self.score[self.team_a] > self.score[self.team_b])

    def test_won(self):
        self.assertTrue(self.score.won(self.team_a))
        self.assertFalse(self.score.won(self.team_b))

    def test_winner(self):
        self.assertEqual(self.team_a, self.score.winner)
