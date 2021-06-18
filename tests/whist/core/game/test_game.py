from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.game.game import Game
from whist.core.game.hand import Hand


class GameTestCase(TeamBaseTestCase):
    def setUp(self):
        super().setUp()
        self.game = Game([self.team_a, self.team_b])

    def test_first_hand(self):
        current_hand = self.game.next_hand()
        self.assertIsInstance(current_hand, Hand)

    def test_second_hand(self):
        first_hand = self.game.next_hand()
        second_hand = self.game.next_hand()
        self.assertNotEqual(first_hand, second_hand)
