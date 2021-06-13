from unittest import skip

from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.game.game import Game


class GameTestCase(TeamBaseTestCase):
    @skip('Not done yet.')
    def test_done(self):
        game = Game(teams=[self.team_a, self.team_b])
        self.assertTrue(game.done)
