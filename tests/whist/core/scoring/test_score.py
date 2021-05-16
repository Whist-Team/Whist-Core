from tests.whist.core.scoring.scoring_base_test_case import ScoringBaseTestCase
from whist.core.scoring.score import Score


class ScoreTestCase(ScoringBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.score = Score([self.team_a, self.team_b], [7, 6])

    def test_score(self):
        self.assertTrue(self.score[self.team_a] > self.score[self.team_b])

    def test_won(self):
        self.assertTrue(self.score.won(self.team_a))
        self.assertFalse(self.score.won(self.team_b))
