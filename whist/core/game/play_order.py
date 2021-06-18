from whist.core.cards.hand import Hand
from whist.core.game.player_at_table import PlayerAtTable
from whist.core.scoring.team import Team


class PlayOrder:
    def __init__(self, teams: list[Team]):
        self._size = len(teams) * len(teams[0].players)
        self._next_player = 0
        self._play_order: list[PlayerAtTable] = [None] * self._size
        for team_index, team in enumerate(teams):
            for player_index, player in enumerate(team.players):
                player_index = team_index + player_index * len(teams)
                self._play_order[player_index] = PlayerAtTable(player, Hand())

    def next_order(self) -> 'PlayOrder':
        return PlayOrder._new_order(self)

    def next_player(self) -> PlayerAtTable:
        player: PlayerAtTable = self._play_order[self._next_player]
        self._next_player = (self._next_player + 1) % self._size
        return player

    @classmethod
    def _new_order(cls, old_order: 'PlayOrder'):
        instance = cls.__new__(cls)
        instance._play_order = old_order._play_order[1:] + old_order._play_order[:1]
        instance._size = len(instance._play_order)
        instance._next_player = 0
        return instance
