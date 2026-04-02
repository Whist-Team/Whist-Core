import unittest

from whist_core.scoring.team import Team
from whist_core.user.player import Player


class TeamBaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.player_a = Player(username="a", rating=1600)
        cls.player_b = Player(username="b", rating=1800)
        cls.player_c = Player(username="c", rating=1700)
        cls.player_d = Player(username="d", rating=1700)

    def setUp(self) -> None:
        self.team_a = Team(players=[self.player_a, self.player_b])
        self.team_b = Team(players=[self.player_c, self.player_d])

    def tearDown(self) -> None:
        self.player_a.rating = 1600
        self.player_b.rating = 1800
        self.player_c.rating = 1700
        self.player_d.rating = 1700
