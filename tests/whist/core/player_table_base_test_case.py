from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.game.play_order import PlayOrder


class PlayerAtTableBaseTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.play_order = PlayOrder([self.team_a, self.team_b])
