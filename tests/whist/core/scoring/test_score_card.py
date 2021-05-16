from tests.whist.core.scoring.scoring_base_test_case import ScoringBaseTestCase
from whist.core.scoring.score import Score
from whist.core.scoring.score_card import ScoreCard


class ScoreCardTestCase(ScoringBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.score_card = ScoreCard()

    def test_add_score(self):
        score = Score([self.team_a, self.team_b], [7, 6])
        self.score_card.add_score(score)
        self.assertEqual(1, len(self.score_card))

    def test_draw(self):
        score = Score([self.team_a, self.team_b], [7, 6])
        self.score_card.add_score(score)
        score = Score([self.team_a, self.team_b], [6, 7])
        self.score_card.add_score(score)
        self.assertEqual(0, self.score_card.won(self.team_a))
