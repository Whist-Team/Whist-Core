from tests.whist_core.team_base_test_case import TeamBaseTestCase
from whist_core.scoring.team import Team


class TeamTestCase(TeamBaseTestCase):
    def test_equal(self):
        expected_team = Team(players=[self.player_a, self.player_b])
        self.assertEqual(expected_team, self.team_a)
