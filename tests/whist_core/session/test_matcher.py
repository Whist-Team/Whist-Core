import unittest

from whist_core.error.matcher_error import NotEnoughPlayersError
from whist_core.session.matcher import RandomMatcher, RoundRobinMatcher
from whist_core.session.userlist import UserList
from whist_core.user.player import Player


class MatchTestCase(unittest.TestCase):
    def setUp(self) -> None:
        player_a = Player(user_id=2, username='a', rating=1)
        player_b = Player(user_id=3, username='b', rating=1)
        player_c = Player(user_id=4, username='c', rating=1)
        player_d = Player(user_id=5, username='d', rating=1)
        self.players = [player_a, player_b, player_c, player_d]
        self.user_list = UserList()
        self.random_matcher = RandomMatcher(self.user_list)
        self.robin_matcher = RoundRobinMatcher(self.user_list)
        for player in self.players:
            self.user_list.append(player)

    def test_random_distribute(self):
        teams = self.random_matcher.distribute(2, 2)
        self.assertEqual(2, len(teams[0].players))
        self.assertEqual(2, len(teams[1].players))
        self.assertEqual(2, self.user_list.team_size(0))
        self.assertEqual(2, self.user_list.team_size(1))

    def test_round_robin_distribute(self):
        teams = self.robin_matcher.distribute(2, 2)
        self.assertEqual(teams[0].players[0], self.players[0])
        self.assertEqual(teams[1].players[0], self.players[1])
        self.assertEqual(teams[0].players[1], self.players[2])
        self.assertEqual(teams[1].players[1], self.players[3])

    def test_round_robin_min_player_distribute(self):
        user_list = UserList()
        user_list.append(self.players[0])
        user_list.append(self.players[1])
        robin_matcher = RoundRobinMatcher(user_list)
        with self.assertRaises(NotEnoughPlayersError):
            _ = robin_matcher.distribute(2, 2)

    def test_zero_players_per_team(self):
        with self.assertRaises(ValueError):
            _ = self.robin_matcher.distribute(num_teams=2, team_size=0)

    def test_zero_teams(self):
        with self.assertRaises(ValueError):
            _ = self.robin_matcher.distribute(num_teams=0, team_size=2)
