"""Ring buffer of players at the table."""
import json
from typing import Optional, Any

from whist.core.cards.card_container import UnorderedCardContainer
from whist.core.game.player_at_table import PlayerAtTable
from whist.core.scoring.team import Team
from whist.core.user.player import Player


class PlayOrder:
    """
    Iterates over the players at the table.
    """

    def __init__(self, play_order: list[PlayerAtTable], next_player: int = 0):
        self._next_player = next_player
        self.play_order = play_order

    def __iter__(self):
        return iter(self.play_order)

    def __eq__(self, other):
        if not isinstance(other, PlayOrder):
            return False
        return self.play_order == other.play_order and self._next_player == other._next_player

    @staticmethod
    def from_team_list(teams: list[Team]):
        size = len(teams) * len(teams[0].players)
        play_order: list[Optional[PlayerAtTable]] = [None] * size
        for team_index, team in enumerate(teams):
            for player_index, player in enumerate(team.players):
                player_index = team_index + player_index * len(teams)
                play_order[player_index] = PlayerAtTable(
                    player=player,
                    hand=UnorderedCardContainer.empty()
                )
        return PlayOrder(play_order, 0)

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

    def next_player(self) -> PlayerAtTable:
        """
            Retrieves the next player who's turn it is.
            :rtype: PlayOrder
            """
        player: PlayerAtTable = self.play_order[self._next_player]
        self._next_player = (self._next_player + 1) % len(self.play_order)
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
        instance = cls.__new__(cls)
        instance.play_order = old_order.play_order[1:] + old_order.play_order[:1]
        instance.size = len(instance.play_order)
        instance._next_player = 0
        return instance

    @classmethod
    def _new_rotate_order(cls, old_order: 'PlayOrder', rotation: int):
        instance = cls.__new__(cls)
        instance.play_order = old_order.play_order[rotation:] + old_order.play_order[:rotation]
        instance.size = len(instance.play_order)
        instance._next_player = 0
        return instance

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, values):
        if isinstance(values, PlayOrder):
            play_order = values.play_order
            next_player = values._next_player
        elif isinstance(values, str):
            json_loads = json.loads(values)
            play_order = json_loads['play_order']
            next_player = json_loads['next_player']
        else:
            raise NotImplementedError
        if not isinstance(play_order[0], PlayerAtTable):
            raise TypeError(f'play order is not list of PlayerAtTable: {play_order}')
        if not isinstance(next_player, int):
            raise TypeError(f'next player: {next_player} is not an int')
        return cls(play_order=play_order, next_player=next_player)

    class PlayOrderEncoder(json.JSONEncoder):
        """
        Custom json encoder to play order.
        """

        def default(self, obj: Any) -> Any:
            """
            Encode the play order to a dictionary, if it is a play order else uses normal json
            encoding.
            :param obj: to be encoded
            :return: dict containing the order of players and the index of the next player
            """
            if isinstance(obj, PlayOrder):
                player_order = [player.json() for player in obj.play_order]
                order_dict = {'play_order': player_order,
                              'next_player': obj._next_player}
                return order_dict
            return json.JSONEncoder.default(self, obj)
