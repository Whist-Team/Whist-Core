import unittest

from whist_core.error.matcher_error import NotEnoughPlayersError
from whist_core.session.matcher import RandomMatcher, RoundRobinMatcher
from whist_core.session.userlist import UserList
from whist_core.user.player import Player


class MatcherTestCase(unittest.TestCase):
    def setUp(self) -> None:
        player_a = Player(user_id=2, username='a', rating=1)
        player_b = Player(user_id=3, username='b', rating=1)
        player_c = Player(user_id=4, username='c', rating=1)
        player_d = Player(user_id=5, username='d', rating=1)
        self.players = [player_a, player_b, player_c, player_d]
        self.user_list = UserList()
        self.random_matcher = RandomMatcher(number_teams=2, team_size=2)
        self.robin_matcher = RoundRobinMatcher(number_teams=2, team_size=2)
        for player in self.players:
            self.user_list.append(player)

    def test_random_distribute(self):
        distribution = self.random_matcher.distribute(self.user_list)
        self.assertEqual(4, len(distribution))
        self.assertEqual(2, len([entry for entry in distribution if entry.team_id == 0]))
        self.assertEqual(2, len([entry for entry in distribution if entry.team_id == 1]))

    def test_round_robin_distribute(self):
        distribution = self.robin_matcher.distribute(self.user_list)
        self.assertEqual(distribution[0].player_index, 0)
        self.assertEqual(distribution[0].team_id, 0)
        self.assertEqual(distribution[1].player_index, 1)
        self.assertEqual(distribution[1].team_id, 0)
        self.assertEqual(distribution[2].player_index, 2)
        self.assertEqual(distribution[2].team_id, 1)
        self.assertEqual(distribution[3].player_index, 3)
        self.assertEqual(distribution[3].team_id, 1)

    def test_round_robin_min_player_distribute(self):
        user_list = UserList()
        user_list.append(self.players[0])
        user_list.append(self.players[1])
        random_matcher = RandomMatcher(number_teams=2, team_size=2)
        with self.assertRaises(NotEnoughPlayersError):
            _ = random_matcher.distribute(user_list)

    def test_second_round_robin(self):
        _ = self.robin_matcher.distribute(self.user_list)
        distribution = self.robin_matcher.distribute(self.user_list)
        self.assertEqual(distribution[0].player_index, 0)
        self.assertEqual(distribution[0].team_id, 0)
        self.assertEqual(distribution[1].player_index, 1)
        self.assertEqual(distribution[1].team_id, 1)
        self.assertEqual(distribution[2].player_index, 2)
        self.assertEqual(distribution[2].team_id, 0)
        self.assertEqual(distribution[3].player_index, 3)
        self.assertEqual(distribution[3].team_id, 1)
