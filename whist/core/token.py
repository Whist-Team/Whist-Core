from datetime import timedelta, datetime

from jose import jwt
from pydantic import BaseModel

from whist.core import SECRET_KEY, ALGORITHM
from whist.core.player import Player


class Token(BaseModel):
    username: str

    @staticmethod
    def create(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({'exp': expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    async def get_user(db, token: str):
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise KeyError('No username in token.')
        token = Token(username=username)
        player = Player.get_player(db, token.username)
        if player is None:
            raise ArithmeticError(f'No user with username: {username} found.')
        return player
