"""DAO of session."""
from whist.core.error.table_error import TableFullError
from whist.core.player import Player
from whist.core.session import Session


class Table(Session):
    """
    The game logics instance of a room to play Whist.
    """
    min_player: int
    max_player: int

    def __len__(self):
        """
        The amount of players joined.
        :return: # player
        :rtype: int
        """
        return len(self._users)

    @property
    def ready(self) -> bool:
        """
        Flag if the table is ready to start playing.
        :return Ready or not
        :rtype: boolean
        """
        return len(self._users) >= self.min_player and self._users.ready

    def join(self, player: Player) -> None:
        """
        If a seat is available a player joins the table.
        :param player: who wants to join the table
        :type player: Player
        :return: None or raised an error if the table is already full.
        :rtype: None
        """
        if len(self._users) < self.max_player:
            self._users.append(player)
        else:
            raise TableFullError(f'Table with ID: {self.session_id} is already full.')

    def leave(self, player: Player) -> None:
        """
        Remove a player from table.
        :param player: The player to remove.
        :type player: Player
        :return: None
        :rtype: None
        """
        self._users.remove(player)

    def player_ready(self, player) -> None:
        """
        Player says they is ready.
        :param player: player who is ready
        :type player: Player
        :return: None
        :rtype: None
        """
        self._users.player_ready(player)

    def player_unready(self, player) -> None:
        """
        Player says they is not ready.
        :param player: player who is not ready
        :type player: Player
        :return: None
        :rtype: None
        """
        self._users.player_unready(player)
