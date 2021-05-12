import unittest

from whist.core.player import Player

USERNAME = 'honk'


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player(**{'user_id': 1, 'username': USERNAME, 'level': 1})
        self.db = {USERNAME: self.player}
