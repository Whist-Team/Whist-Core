from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str


class Player(User):
    level: int

    @staticmethod
    def get_player(db, username: str) -> Optional['Player']:
        if username in db:
            user: Player = db[username]
            return Player(**user.dict())
        return None
