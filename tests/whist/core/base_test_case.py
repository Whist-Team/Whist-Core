import unittest

from whist.core.player import Player
from whist.core.user import User

USERNAME = 'honk'


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        user = User(user_id=1, username=USERNAME)
        user_dict: dict = user.dict()
        user_dict.update({'level': 1})
        self.player = Player(**user_dict)
        self.db = {USERNAME: self.player}
