from tests.whist.core.base_test_case import BaseTestCase, USERNAME
from core.user.player import Player


class PlayerTestCase(BaseTestCase):
    def test_str(self):
        self.assertEqual(USERNAME, str(self.player))

    def test_get_player(self):
        player = Player.get_player(self.db, USERNAME)
        self.assertIsNotNone(player)

    def test_not_found(self):
        player = Player.get_player(self.db, 'abc')
        self.assertIsNone(player)
