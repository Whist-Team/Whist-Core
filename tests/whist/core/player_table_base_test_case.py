from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.cards.hand import Hand
from whist.core.game.play_order import PlayOrder
from whist.core.game.player_at_table import PlayerAtTable


class PlayerAtTableBaseTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.play_order = PlayOrder([self.team_a, self.team_b])
        self.player_order: list[PlayerAtTable] = [PlayerAtTable(self.player_a, Hand.empty()),
                                                  PlayerAtTable(self.player_c, Hand.empty()),
                                                  PlayerAtTable(self.player_b, Hand.empty()),
                                                  PlayerAtTable(self.player_d, Hand.empty())]
