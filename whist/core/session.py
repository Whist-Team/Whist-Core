"""DTO of a game room"""
from pydantic import BaseModel

from whist.core.userlist import UserList


class Session(BaseModel):
    """
    User can join to play a game of Whist.
    """
    session_id: int
    users: UserList = []

    class Config:
        arbitrary_types_allowed = True
