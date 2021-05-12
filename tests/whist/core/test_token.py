import asyncio
from datetime import timedelta, datetime

from jose import jwt

from tests.whist.core.base_test_case import USERNAME, BaseTestCase
from whist.core import SECRET_KEY, ALGORITHM
from whist.core.token import Token


class TokenTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.payload = dict(sub=USERNAME)
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

    def test_wrong_key(self):
        with self.assertRaises(KeyError):
            token = Token.create(dict(wrong=USERNAME))
            loop = asyncio.get_event_loop()
            _ = loop.run_until_complete(Token.get_user(self.db, token))
            loop.close()

    def test_no_username(self):
        with self.assertRaises(ValueError):
            token = Token.create(dict(sub='abc'))
            loop = asyncio.get_event_loop()
            _ = loop.run_until_complete(Token.get_user(self.db, token))
            loop.close()

    def test_expired_token(self):
        token = Token.create(self.payload, expires_delta=timedelta(minutes=-1))
        with self.assertRaises(jwt.ExpiredSignatureError):
            _ = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
