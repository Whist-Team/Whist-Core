import unittest

from whist.core.session.matcher import RandomMatch
from whist.core.session.userlist import UserList
from whist.core.user.player import Player


class MatchTestCase(unittest.TestCase):
    def setUp(self) -> None:
        player_a = Player(user_id=2, username='a', rating=1)
        player_b = Player(user_id=3, username='b', rating=1)
        player_c = Player(user_id=4, username='c', rating=1)
        player_d = Player(user_id=5, username='d', rating=1)
        self.players = [player_a, player_b, player_c, player_d]
        self.user_list = UserList()
        for player in self.players:
            self.user_list.append(player)

    def test_distribute(self):
        matcher = RandomMatch(2, 2, self.user_list)
        matcher.distribute()
        self.assertEqual(2, self.user_list.team_size(0))
        self.assertEqual(2, self.user_list.team_size(1))
