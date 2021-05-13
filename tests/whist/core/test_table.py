from tests.whist.core.base_test_case import BaseTestCase
from whist.core.table import Table


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
        self.assertEqual(1, len(self.table.users))

    def test_leave(self):
        self.table.join(self.player)
        self.table.leave(self.player)
        self.assertEqual(0, len(self.table.users))
