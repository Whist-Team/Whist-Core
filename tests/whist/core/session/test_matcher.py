from tests.whist.core.base_test_case import BaseTestCase
from whist.core.session.matcher import RandomMatch
from whist.core.session.userlist import UserList
from whist.core.user.player import Player


class MatchTestCase(BaseTestCase):
    def test_distribute(self):
        player_a = Player(user_id=2, username='a', level=1)
        player_b = Player(user_id=3, username='b', level=1)
        player_c = Player(user_id=4, username='c', level=1)
        player_d = Player(user_id=5, username='d', level=1)
        players = [player_a, player_b, player_c, player_d]
        user_list = UserList()
        for player in players:
            user_list.append(player)

        matcher = RandomMatch(2, 2, user_list)
        matcher.distribute()
        self.assertEqual(2, user_list.team_size(0))
        self.assertEqual(2, user_list.team_size(1))
