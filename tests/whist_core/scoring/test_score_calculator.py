from unittest.mock import MagicMock

from tests.whist_core.team_base_test_case import TeamBaseTestCase
from whist_core.cards.card_container import UnorderedCardContainer
from whist_core.game.play_order import PlayOrder
from whist_core.game.player_at_table import PlayerAtTable
from whist_core.scoring.score import Score
from whist_core.scoring.score_calculator import ScoreCalculator


class TestScoreCalculator(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.table_player_a = PlayerAtTable(team=0, player=self.player_a,
                                            hand=UnorderedCardContainer.empty())
        self.table_player_b = PlayerAtTable(team=0, player=self.player_b,
                                            hand=UnorderedCardContainer.empty())
        self.table_player_c = PlayerAtTable(team=1, player=self.player_c,
                                            hand=UnorderedCardContainer.empty())
        self.table_player_d = PlayerAtTable(team=1, player=self.player_d,
                                            hand=UnorderedCardContainer.empty())

        tricks = []
        for _ in range(0, 7):
            trick = MagicMock(winner=self.table_player_a)
            tricks.append(trick)
        for _ in range(0, 6):
            trick = MagicMock(winner=self.table_player_c)
            tricks.append(trick)
        self.hand = MagicMock(tricks=tricks)

    def test_single_score(self):
        play_order = PlayOrder.from_team_list([self.team_a, self.team_b])
        expected_score = Score(scores=[1, 0], teams=[self.team_a, self.team_b])
        score = ScoreCalculator.calc_score(self.hand, play_order)
        self.assertEqual(expected_score, score)

    def test_count_wins(self):
        self.assertEqual([1, 0], ScoreCalculator.calc_score_raw(self.hand))
