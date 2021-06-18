from whist.core.scoring.team import Team
from whist.core.user.player import Player


class PlayOrder:
    def __init__(self, teams: list[Team]):
        self._size = len(teams)
        self._next_player = 0
        self._play_order: list[Player] = [None] * self._size * len(teams[0].players)
        for team_index, team in enumerate(teams):
            for player_index, player in enumerate(team.players):
                self._play_order[team_index + player_index * self._size] = player

    def next_order(self) -> None:
        self._play_order = self._play_order[1:] + self._play_order[:1]

    def next_player(self) -> Player:
        player: Player = self._play_order[self._next_player]
        self._next_player = (self._next_player + 1) % self._size
        return player
