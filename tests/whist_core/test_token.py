import asyncio
from datetime import timedelta, datetime

import pytest
from jose import jwt

from tests.whist_core.base_test_case import USERNAME, BaseTestCase
from whist_core import SECRET_KEY, ALGORITHM
from whist_core.token import Token


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

    @pytest.mark.asyncio
    async def test_wrong_key(self):
        with self.assertRaises(KeyError):
            token = Token.create(dict(wrong=USERNAME))
            _ = await Token.get_user(self.db, token)

    @pytest.mark.asyncio
    async def test_no_username(self):
        token = Token.create(dict(sub='abc'))
        with self.assertRaises(ValueError):
            _ = await Token.get_user(self.db, token)

    def test_expired_token(self):
        token = Token.create(self.payload, expires_delta=timedelta(minutes=-1))
        with self.assertRaises(jwt.ExpiredSignatureError):
            _ = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
