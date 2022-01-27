"""Ring buffer of players at the table."""
from typing import Optional

from pydantic import BaseModel

from whist.core.cards.card_container import UnorderedCardContainer
from whist.core.game.player_at_table import PlayerAtTable
from whist.core.scoring.team import Team
from whist.core.user.player import Player


class PlayOrder(BaseModel):
    """
    Iterates over the players at the table.
    """

    next_player: int
    play_order: list[PlayerAtTable]

    def __iter__(self):
        return iter(self.play_order)

    def __eq__(self, other):
        if not isinstance(other, PlayOrder):
            return False
        return self.play_order == other.play_order and self.next_player == other.next_player

    @staticmethod
    def from_team_list(teams: list[Team]):
        """
        Factory method to create a play order from a team list.
        :param teams: list of teams
        :return: PlayOrder
        """
        size = len(teams) * len(teams[0].players)
        play_order: list[Optional[PlayerAtTable]] = [None] * size
        for team_index, team in enumerate(teams):
            for player_index, player in enumerate(team.players):
                player_index = team_index + player_index * len(teams)
                play_order[player_index] = PlayerAtTable(
                    player=player,
                    hand=UnorderedCardContainer.empty()
                )
        return PlayOrder(play_order=play_order, next_player=0)

    def rotate(self, player: PlayerAtTable) -> 'PlayOrder':
        """
            Rotates the play order, so the player will be next player.
            :param player: who should be at beginning of the play order
            :return: None
            """
        order = list(self)
        rotation: int = order.index(player)
        return PlayOrder._new_rotate_order(self, rotation)

    def next_order(self) -> 'PlayOrder':
        """
            Create the order for the next hand.
            :rtype: PlayOrder
            """
        return PlayOrder._new_order(self)

    def get_next_player(self) -> PlayerAtTable:
        """
            Retrieves the next player who's turn it is.
            :rtype: PlayOrder
            """
        player: PlayerAtTable = self.play_order[self.next_player]
        self.next_player = (self.next_player + 1) % len(self.play_order)
        return player

    def get_player(self, player: Player) -> PlayerAtTable:
        """
            Retrieves the PlayerAtTable for the player given.
            :param player: who needs it's counterpart at the table
            :return: the player at table
            """
        return [table_player for table_player in self.play_order
                if table_player.player == player][0]

    # pylint: disable=protected-access
    @classmethod
    def _new_order(cls, old_order: 'PlayOrder'):
        play_order = old_order.play_order[1:] + old_order.play_order[:1]
        next_player = 0
        return PlayOrder(play_order=play_order, next_player=next_player)

    @classmethod
    def _new_rotate_order(cls, old_order: 'PlayOrder', rotation: int):
        play_order = old_order.play_order[rotation:] + old_order.play_order[:rotation]
        next_player = 0
        return PlayOrder(play_order=play_order, next_player=next_player)
