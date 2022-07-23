from tests.whist_core.base_test_case import BaseTestCase, USERNAME
from whist_core.error.player_error import NegativeRatingError
from whist_core.user.player import Player


class PlayerTestCase(BaseTestCase):
    def test_str(self):
        self.assertEqual(USERNAME, str(self.player))

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
        
    def test_negative_rating(self):
        with self.assertRaises(NegativeRTingError):
            Player(user_id=3, username='negative', rating=-1)
