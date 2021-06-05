from tests.whist.core.base_test_case import BaseTestCase
from whist.core.session.userlist import UserList
from whist.core.user.player import Player


class UserListTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user_list = UserList()

    def test_ready(self):
        self.user_list.append(self.player)
        self.user_list.player_ready(self.player)
        self.assertTrue(self.user_list.ready)

    def test_not_ready(self):
        self.user_list.append(self.player)
        self.user_list.player_ready(self.player)
        self.user_list.player_unready(self.player)
        self.assertFalse(self.user_list.ready)

    def test_append(self):
        self.user_list.append(self.player)
        self.assertEqual(1, len(self.user_list))

    def test_remove(self):
        self.user_list.append(self.player)
        self.user_list.remove(self.player)
        self.assertEqual(0, len(self.user_list))

    def test_join_team(self):
        self.user_list.append(self.player)
        self.user_list.change_team(self.player, 1)
        self.assertEqual(1, self.user_list.team(self.player))

    def test_change_team(self):
        self.user_list.append(self.player)
        self.user_list.change_team(self.player, 2)
        self.user_list.change_team(self.player, 1)
        self.assertEqual(1, self.user_list.team(self.player))

    def test_team_size(self):
        self.user_list.append(self.player)
        self.user_list.change_team(self.player, 1)
        self.assertEqual(1, self.user_list.team_size(1))

    def test_team_size_two_teams(self):
        player = Player(user_id=2, username='hank', level=1)
        self.user_list.append(self.player)
        self.user_list.append(player)
        self.user_list.change_team(self.player, 1)
        self.user_list.change_team(player, 2)
        self.assertEqual(1, self.user_list.team_size(1))
        self.assertEqual(1, self.user_list.team_size(2))

    def test_team_size_same_team(self):
        player = Player(user_id=2, username='hank', level=1)
        self.user_list.append(self.player)
        self.user_list.append(player)
        self.user_list.change_team(self.player, 1)
        self.user_list.change_team(player, 1)
        self.assertEqual(2, self.user_list.team_size(1))

    def test_players(self):
        self.user_list.append(self.player)
        self.assertSetEqual({self.player}, set(self.user_list.players))
