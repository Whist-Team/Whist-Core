from unittest.mock import patch, PropertyMock

from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.game.rubber import Rubber
from whist.core.session.userlist import UserList


class RubberTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.rubber = Rubber(teams=[self.team_a, self.team_b])

    def test_not_done(self):
        self.assertFalse(self.rubber.done)

    def test_done(self):
        with patch('whist.core.game.game.Game.done',
                   new_callable=PropertyMock(return_value=True)):
            _ = self.rubber.next_game()
            _ = self.rubber.next_game()
            _ = self.rubber.next_game()
        self.assertTrue(self.rubber.done)

    def test_create_random(self):
        players = [self.player_a, self.player_b, self.player_c, self.player_d]
        user_list = UserList()
        for player in players:
            user_list.append(player)
        rubber = Rubber.create_random(user_list, 2, 2)
        self.assertEqual(2, len(rubber.teams))
        self.assertIn(self.player_a, rubber.teams[0].players)
        self.assertIn(self.player_b, rubber.teams[0].players)
        self.assertIn(self.player_c, rubber.teams[1].players)
        self.assertIn(self.player_d, rubber.teams[1].players)
