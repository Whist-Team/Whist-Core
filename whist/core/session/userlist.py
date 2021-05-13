"""
Handles users joining and leaving a table.
"""
from typing import Optional

from whist.core.user.player import Player
from whist.core.user.status import Status


class UserList:
    """
    User handler for tables.
    """
    _users: dict[Player] = {}

    def __len__(self):
        return len(self._users)

    @property
    def ready(self) -> bool:
        """
        Returns if all players are ready.
        :return: Ready or not
        :rtype: boolean
        """
        player_status: Status
        for player_status in self._users.values():
            if not player_status.ready:
                return False
        return True

    def team(self, player: Player) -> Optional[int]:
        """
        Gets the id of the team for a player.
        :param player: for which the id should be retrieved
        :type player: Player
        :return: Integer if player joined a team or None if not.
        :rtype: int
        """
        status: Status = self._users.get(player)
        return status.team

    def append(self, player: Player):
        """
        Adds a player to the list.
        :param player: player to join
        :type player: Player
        :return: None
        :rtype: None
        """
        self._users.update({player: Status()})

    def remove(self, player: Player):
        """
        Removes the player from the list.
        :param player: player to leave
        :type player: Player
        :return: None
        :rtype: None
        """
        self._users.pop(player)

    def change_team(self, player: Player, team: int) -> None:
        """
        Player changes teams.
        :param player: to change teams
        :type player: Player
        :param team: id of the new team
        :type team: int
        :return: None
        :rtype: None
        """
        status: Status = self._users.get(player)
        status.team = team

    def player_ready(self, player: Player):
        """
        Player says they is ready.
        :param player: player who is ready
        :type player: Player
        :return: None
        :rtype: None
        """
        status: Status = self._users.get(player)
        status.ready = True

    def player_unready(self, player: Player):
        """
        Player says they is not ready.
        :param player: player who is not ready
        :type player: Player
        :return: None
        :rtype: None
        """
        status: Status = self._users.get(player)
        status.ready = False
