"""DTO of a game room"""
from pydantic import BaseModel

from whist.core.player import Player


class Session(BaseModel):
    """
    User can join to play a game of Whist.
    """
    session_id: int
    users: list[Player]
