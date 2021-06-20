from unittest.mock import patch, PropertyMock

from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.game.rubber import Rubber


class RubberTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.rubber = Rubber(teams=[self.team_a, self.team_b])

    def test_not_done(self):
        self.assertFalse(self.rubber.done)

    def test_done(self):
        with patch('whist.core.game.game.Game.done',
                   new_callable=PropertyMock(return_value=True)):
            _ = self.rubber.next_game()
            _ = self.rubber.next_game()
            _ = self.rubber.next_game()
        self.assertTrue(self.rubber.done)
