import json

from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.game.play_order import PlayOrder


class PlayOrderTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.order = PlayOrder([self.team_a, self.team_b])

    def test_next_order(self):
        next_order: PlayOrder = self.order.next_order()
        self.assertEqual(self.team_b.players[0], next_order.next_player().player)

    def test_next_order_immutable(self):
        next_order: PlayOrder = self.order.next_order()
        second_next_order: PlayOrder = self.order.next_order()
        self.assertEqual(next_order, second_next_order)

    def test_next_player(self):
        self.assertEqual(self.team_a.players[0], self.order.next_player().player)
        self.assertEqual(self.team_b.players[0], self.order.next_player().player)
        self.assertEqual(self.team_a.players[1], self.order.next_player().player)
        self.assertEqual(self.team_b.players[1], self.order.next_player().player)

    def test_json(self):
        expected_json = {'play_order':
            [
                self.team_a.players[0].username,
                self.team_b.players[0].username,
                self.team_a.players[1].username,
                self.team_b.players[1].username,
            ],
            'next_player': 0}
        order_json = json.dumps(self.order)
        self.assertEqual(expected_json, order_json)
