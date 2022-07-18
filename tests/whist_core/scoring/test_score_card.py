from tests.whist_core.team_base_test_case import TeamBaseTestCase
from whist_core.scoring.score import Score
from whist_core.scoring.score_card import ScoreCard


class ScoreCardTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.score_card = ScoreCard()

    def test_add_score(self):
        score = Score([self.team_a, self.team_b], [1, 0])
        self.score_card.add_score(score)
        self.assertEqual(1, len(self.score_card))
        self.assertEqual(1, self.score_card.score(self.team_a))
        self.assertEqual(0, self.score_card.score(self.team_b))

    def test_draw(self):
        score = Score([self.team_a, self.team_b], [1, 0])
        self.score_card.add_score(score)
        score = Score([self.team_a, self.team_b], [0, 1])
        self.score_card.add_score(score)
        self.assertEqual(0, self.score_card.won(self.team_a))

    def test_max(self):
        score = Score([self.team_a, self.team_b], [1, 0])
        self.score_card.add_score(score)
        score = Score([self.team_a, self.team_b], [0, 1])
        self.score_card.add_score(score)
        score = Score([self.team_a, self.team_b], [0, 1])
        self.score_card.add_score(score)
        self.assertEqual(2, self.score_card.max)

    def test_max_without_hand(self):
        self.assertEqual(0, self.score_card.max)
