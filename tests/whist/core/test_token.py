import asyncio
import unittest
from datetime import timedelta, datetime

from jose import jwt

from whist.core import SECRET_KEY, ALGORITHM
from whist.core.player import Player
from whist.core.token import Token
from whist.core.user import User

USERNAME = 'honk'


class TokenTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = dict(sub=USERNAME)
        user = User(user_id=1, username=USERNAME)
        user_dict: dict = user.dict()
        user_dict.update({'level': 1})
        self.player = Player(**user_dict)
        self.db = {USERNAME: self.player}
        self.token = Token.create(self.payload, expires_delta=timedelta(minutes=2))

    def test_create(self):
        payload = jwt.decode(self.token, SECRET_KEY, algorithms=[ALGORITHM])
        self.assertEqual(USERNAME, payload['sub'])
        self.assertLess(datetime.utcnow(), datetime.fromtimestamp(payload['exp']))

    def test_get_user(self):
        loop = asyncio.get_event_loop()
        user = loop.run_until_complete(Token.get_user(self.db, self.token))
        loop.close()
        self.assertEqual(self.player, user)

    def test_expired_token(self):
        token = Token.create(self.payload, expires_delta=timedelta(minutes=-1))
        with self.assertRaises(jwt.ExpiredSignatureError):
            _ = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
