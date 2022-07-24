from tests.whist_core.team_base_test_case import TeamBaseTestCase
from whist_core.game.play_order import PlayOrder


class PlayOrderTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.order = PlayOrder.from_team_list([self.team_a, self.team_b])

    def test_next_order(self):
        next_order: PlayOrder = self.order.next_order()
        self.assertEqual(self.team_b.players[0], next_order.get_next_player().player)

    def test_next_order_immutable(self):
        next_order: PlayOrder = self.order.next_order()
        second_next_order: PlayOrder = self.order.next_order()
        self.assertEqual(next_order, second_next_order)

    def test_next_player(self):
        self.assertEqual(self.team_a.players[0], self.order.get_next_player().player)
        self.assertEqual(self.team_b.players[0], self.order.get_next_player().player)
        self.assertEqual(self.team_a.players[1], self.order.get_next_player().player)
        self.assertEqual(self.team_b.players[1], self.order.get_next_player().player)

    def test_to_team_list(self):
        players_by_team = self.order.to_team_list()
        self.assertEqual([[self.player_a, self.player_b], [self.player_c, self.player_d]],
                         players_by_team)
