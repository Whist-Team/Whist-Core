import unittest

from whist_core.user.player import Player

USERNAME = 'honk'


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player(user_id=1, username=USERNAME, rating=1)
        self.db = {USERNAME: self.player}
