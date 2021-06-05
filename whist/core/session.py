"""DTO of a game room"""
from pydantic import BaseModel

from whist.core.userlist import UserList


class Session(BaseModel):
    """
    User can join to play a game of Whist.
    """
    session_id: int
    _users: UserList = UserList()

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Configuration class for pydantic.
        """
        arbitrary_types_allowed = True
