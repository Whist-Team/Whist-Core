from tests.whist_core.base_test_case import BaseTestCase
from whist_core.error.table_error import TeamFullError, TableFullError, TableNotReadyError, \
    TableNotStartedError, PlayerNotJoinedError
from whist_core.game.rubber import Rubber
from whist_core.session.matcher import RandomMatcher, RoundRobinMatcher
from whist_core.session.table import Table
from whist_core.user.player import Player


class TableTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.table = Table(name='test table', min_player=1, max_player=4)

    def test_ready(self):
        self.table.join(self.player)
        self.table.player_ready(self.player)
        self.assertTrue(self.table.ready)

    def test_not_ready(self):
        self.table.join(self.player)
        self.table.player_ready(self.player)
        self.table.player_unready(self.player)
        self.assertFalse(self.table.ready)

    def test_not_ready_min_player(self):
        table = Table(name='test table', min_player=2, max_player=4)
        table.join(self.player)
        table.player_ready(self.player)
        self.assertFalse(table.ready)

    def test_ready_player_not_joined(self):
        with self.assertRaises(PlayerNotJoinedError):
            self.table.player_ready(self.player)

    def test_unready_player_not_joined(self):
        with self.assertRaises(PlayerNotJoinedError):
            self.table.player_unready(self.player)

    def test_join(self):
        self.table.join(self.player)
        self.assertEqual(1, len(self.table))

    def test_leave(self):
        self.table.join(self.player)
        self.table.leave(self.player)
        self.assertEqual(0, len(self.table))

    def test_join_full_team(self):
        self.table.team_size = 1
        player = Player(user_id=2, username='hank', rating=1)
        self.table.join(self.player)
        self.table.join_team(self.player, 1)
        with self.assertRaises(TeamFullError):
            self.table.join_team(player, 1)

    def test_join_full_table(self):
        self.table.max_player = 1
        player = Player(user_id=2, username='hank', rating=1)
        self.table.join(self.player)
        self.table.join_team(self.player, 1)
        with self.assertRaises(TableFullError):
            self.table.join(player)

    def test_conversion(self):
        self.table.join(self.player)
        table_dict = self.table.dict()
        table = Table(**table_dict)
        self.assertEqual(self.table, table)

    def test_start_random(self):
        second_player = Player(username='miles', rating=3000)
        self.table.join(self.player)
        self.table.join(second_player)
        self.table.player_ready(self.player)
        self.table.player_ready(second_player)
        self.table.start(RandomMatcher)
        self.assertTrue(self.table.started)
        self.assertIsInstance(self.table.current_rubber, Rubber)

    def test_start_robin(self):
        second_player = Player(username='miles', rating=3000)
        self.table.join(self.player)
        self.table.join(second_player)
        self.table.player_ready(self.player)
        self.table.player_ready(second_player)
        self.table.start(RoundRobinMatcher)
        self.assertTrue(self.table.started)
        self.assertIsInstance(self.table.current_rubber, Rubber)

    def test_not_ready_start(self):
        self.table.join(self.player)
        with self.assertRaises(TableNotReadyError):
            self.table.start(RandomMatcher)
        self.assertFalse(self.table.started)

    def test_rubber_without_start(self):
        with self.assertRaises(TableNotStartedError):
            _ = self.table.current_rubber
