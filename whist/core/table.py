from whist.core.error.table_error import TableFullError
from whist.core.player import Player
from whist.core.session import Session


class Table(Session):
    min_player: int
    max_player: int

    @property
    def ready(self) -> bool:
        """
        Flag if the table is ready to start playing.
        :return Ready or not
        :rtype: boolean
        """
        return len(self.users) >= self.min_player

    def join(self, player: Player) -> None:
        """
        If a seat is available a player joins the table.
        :param player: who wants to join the table
        :type player: Player
        :return: None
        :rtype: None
        """
        if len(self.users) < self.max_player:
            self.users.append(player)
        else:
            raise TableFullError(f'Table with ID: {self.session_id} is already full.')
