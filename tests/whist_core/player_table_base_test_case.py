from tests.whist_core.team_base_test_case import TeamBaseTestCase
from whist_core.cards.card_container import UnorderedCardContainer
from whist_core.game.play_order import PlayOrder
from whist_core.game.player_at_table import PlayerAtTable


class PlayerAtTableBaseTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.play_order = PlayOrder.from_team_list([self.team_a, self.team_b])
        self.player_order: list[PlayerAtTable] = [
            PlayerAtTable(player=self.player_a, hand=UnorderedCardContainer.empty(), team=0),
            PlayerAtTable(player=self.player_c, hand=UnorderedCardContainer.empty(), team=0),
            PlayerAtTable(player=self.player_b, hand=UnorderedCardContainer.empty(), team=1),
            PlayerAtTable(player=self.player_d, hand=UnorderedCardContainer.empty(), team=1)]
