from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.cards.card_container import UnorderedCardContainer
from whist.core.game.play_order import PlayOrder
from whist.core.game.player_at_table import PlayerAtTable


class PlayerAtTableBaseTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.play_order = PlayOrder([self.team_a, self.team_b])
        self.player_order: list[PlayerAtTable] = [
            PlayerAtTable(player=self.player_a, hand=UnorderedCardContainer.empty()),
            PlayerAtTable(player=self.player_c, hand=UnorderedCardContainer.empty()),
            PlayerAtTable(player=self.player_b, hand=UnorderedCardContainer.empty()),
            PlayerAtTable(player=self.player_d, hand=UnorderedCardContainer.empty())]
