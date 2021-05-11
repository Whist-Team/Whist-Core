from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str


class Player(User):
    level: int

    @staticmethod
    def get_player(database: dict, username: str) -> Optional['Player']:
        if username in database:
            user: Player = database[username]
            return Player(**user.dict())
        return None
