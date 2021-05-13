from tests.whist.core.base_test_case import BaseTestCase
from whist.core.error.table_error import TeamFullError
from whist.core.session.table import Table
from whist.core.user.player import Player


class TableTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.table = Table(session_id=1, min_player=1, max_player=4)

    def test_ready(self):
        self.table.join(self.player)
        self.table.player_ready(self.player)
        self.assertTrue(self.table.ready)

    def test_not_ready(self):
        self.table.join(self.player)
        self.table.player_ready(self.player)
        self.table.player_unready(self.player)
        self.assertFalse(self.table.ready)

    def test_join(self):
        self.table.join(self.player)
        self.assertEqual(1, len(self.table))

    def test_leave(self):
        self.table.join(self.player)
        self.table.leave(self.player)
        self.assertEqual(0, len(self.table))

    def test_join_full_team(self):
        self.table.team_size = 1
        player = Player(user_id=2, username='hank', level=1)
        self.table.join(self.player)
        self.table.join_team(self.player, 1)
        with self.assertRaises(TeamFullError):
            self.table.join_team(player, 1)
        self.table.leave(player)
