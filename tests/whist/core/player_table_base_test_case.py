from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.cards.hand import Hand
from whist.core.game.player_at_table import PlayerAtTable


class PlayerAtTableBaseTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUpClass()
        self.play_order: list[PlayerAtTable] = [PlayerAtTable(self.player_a, Hand.empty()),
                                                PlayerAtTable(self.player_c, Hand.empty()),
                                                PlayerAtTable(self.player_b, Hand.empty()),
                                                PlayerAtTable(self.player_d, Hand.empty())]
