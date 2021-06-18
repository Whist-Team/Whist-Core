from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.game.rubber import Rubber


class RubberTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.rubber = Rubber(teams=[self.team_a, self.team_b])

    def test_rubber_not_done(self):
        self.assertFalse(self.rubber.done)
