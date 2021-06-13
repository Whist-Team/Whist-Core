"""Rubber of whist"""
from pydantic import BaseModel


class Rubber(BaseModel):
    """
    Implementation of a rubber.
    """
    max_games: int = 3
    _games_played = 0

    @property
    def games_played(self) -> int:
        """
        Amounts of games played already.
        :rtype: int
        """
        return self._games_played

    @property
    def done(self) -> bool:
        """
        Checks if the rubber is done.
        :return: True if done else Falsee
        :rtype: bool
        """
        return self.games_played == 3
