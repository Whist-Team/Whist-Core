from whist.core.scoring.score import Score
from whist.core.scoring.scoring_base_test_case import ScoringBaseTestCase


class ScoreTestCase(ScoringBaseTestCase):

    def test_score(self):
        score = Score([self.team_a, self.team_b], [7, 6])
        self.assertTrue(score[self.team_a] > score[self.team_b])
