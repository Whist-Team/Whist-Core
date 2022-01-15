from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.cards.card_container import UnorderedCardContainer
from whist.core.game.play_order import PlayOrder
from whist.core.game.player_at_table import PlayerAtTable


class PlayerAtTableBaseTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.play_order = PlayOrder([self.team_a, self.team_b])
        self.player_order: list[PlayerAtTable] = [PlayerAtTable(self.player_a, UnorderedCardContainer.empty()),
                                                  PlayerAtTable(self.player_c, UnorderedCardContainer.empty()),
                                                  PlayerAtTable(self.player_b, UnorderedCardContainer.empty()),
                                                  PlayerAtTable(self.player_d, UnorderedCardContainer.empty())]
