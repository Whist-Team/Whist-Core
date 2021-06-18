from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.game.game import Game
from whist.core.game.hand import Hand


class GameTestCase(TeamBaseTestCase):
    def test_first_hand(self):
        game = Game([self.team_a, self.team_b])
        current_hand = game.next_hand()
        self.assertIsInstance(current_hand, Hand)
