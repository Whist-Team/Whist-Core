"""DAO of user."""
from typing import Optional

from whist.core.user import User


class Player(User):
    """
    This is the server side class of an user.
    """
    level: int

    @staticmethod
    def get_player(database: dict, username: str) -> Optional['Player']:
        """
        Returns a player for a given username if they are in the given database.
        :param database: where to look for the user
        :type database: dictionary
        :param username: the name of the user to look for
        :type username: string
        :return: The player instance or None
        :rtype: Player or None
        """
        if username in database:
            return database[username]
        return None
