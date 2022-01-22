import unittest

from whist.core.error.matcher_error import NotEnoughPlayersError
from whist.core.session.matcher import RandomMatcher, RoundRobinMatcher, Matcher
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

    def test_random_distribute(self):
        teams = RandomMatcher.distribute(2, 2, self.user_list)
        self.assertEqual(2, len(teams[0].players))
        self.assertEqual(2, len(teams[1].players))
        self.assertEqual(2, self.user_list.team_size(0))
        self.assertEqual(2, self.user_list.team_size(1))

    def test_round_robin_distribute(self):
        teams = RoundRobinMatcher.distribute(2, 2, self.user_list)
        self.assertEqual(teams[0].players[0], self.players[0])
        self.assertEqual(teams[1].players[0], self.players[1])
        self.assertEqual(teams[0].players[1], self.players[2])
        self.assertEqual(teams[1].players[1], self.players[3])

    def test_round_robin_min_player_distribute(self):
        user_list = UserList()
        user_list.append(self.players[0])
        user_list.append(self.players[1])
        with self.assertRaises(NotEnoughPlayersError):
            _ = RoundRobinMatcher.distribute(2, 2, user_list)

    def test_abstract(self):
        with self.assertRaises(NotImplementedError):
            Matcher.distribute(1, 2, self.user_list)
