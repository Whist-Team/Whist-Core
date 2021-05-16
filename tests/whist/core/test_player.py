from tests.whist.core.base_test_case import BaseTestCase, USERNAME
from whist.core.player import Player


class PlayerTestCase(BaseTestCase):
    def test_get_player(self):
        player = Player.get_player(self.db, USERNAME)
        self.assertIsNotNone(player)

    def test_not_found(self):
        player = Player.get_player(self.db, 'abc')
        self.assertIsNone(player)

    def test_equal(self):
        player = Player.get_player(self.db, USERNAME)
        self.assertEqual(player, player)

    def test_not_equal(self):
        player = Player.get_player(self.db, USERNAME)
        other = Player(user_id=2, username='other', rating=2000)
        self.assertNotEqual(player, other)

    def test_username(self):
        player = Player.get_player(self.db, USERNAME)
        self.assertEqual(player.username, str(player))
