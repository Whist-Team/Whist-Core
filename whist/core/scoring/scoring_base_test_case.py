import unittest

from whist.core.player import Player
from whist.core.scoring.team import Team


class ScoringBaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        player_a = Player(user_id=2, username='a', rating=1600)
        player_b = Player(user_id=3, username='b', rating=1800)
        player_c = Player(user_id=4, username='c', rating=1700)
        player_d = Player(user_id=5, username='d', rating=1700)
        self.team_a = Team(players=[player_a, player_b])
        self.team_b = Team(players=[player_c, player_d])
