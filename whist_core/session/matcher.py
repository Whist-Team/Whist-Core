"""
Match making tool.
"""
import abc
import random
from typing import Dict

from whist_core.error.matcher_error import NotEnoughPlayersError
from whist_core.scoring.team import Team
from whist_core.session.distribution import Distribution, DistributionEntry
from whist_core.session.userlist import UserList


# pylint: disable=too-few-public-methods
class Matcher(abc.ABC):
    """
    Abstrakt class for player to teams matching.
    """
    teams: list[Distribution] = []

    @abc.abstractmethod
    def distribute(self, num_teams: int, team_size: int, users: UserList) -> list[Team]:
        """
        Distributes cards according to subclass implementation.
        :param num_teams: the amount of teams
        :param team_size: how many players per team
        :param users: the players to be distributed to teams
        :return: the list of teams with players distributed to them
        """
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        """
        Checks if the objects are of the same class.
        :param other: to be checked
        :return: True if same class else False
        """
        return isinstance(other, self.__class__)

    @staticmethod
    def _apply_distribution(distribution, users):
        for entry in distribution:
            users.change_team(users.players[entry.player_index], entry.team_id)


class RoundRobinMatcher(Matcher):
    """
    Distributes the players in the order of the user list.
    """

    def distribute(self, num_teams: int, team_size: int, users: UserList) -> list[Team]:
        """
        Distributes one player to each team each round in order of the user list. Repeats until
        the user list is empty.
        :param num_teams: the amount of teams
        :param team_size: how many players per team
        :param users: the players to be distributed to teams
        :return: the teams in round robin distribution
        """
        if team_size <= 0:
            raise ValueError('The team size must be positive.')
        if num_teams <= 0:
            raise ValueError('There must be at least one team.')
        players = users.players
        if num_teams * team_size > len(players):
            raise NotEnoughPlayersError(f'{num_teams * team_size} of players are need, but only '
                                        f'{len(players)} have joined.')
        distribution = Distribution()
        team_id = 0
        for player_index in range(len(players)):
            entry = DistributionEntry(player_index=player_index, team_id=team_id)
            distribution.add(entry)
            team_id = (team_id + 1) % num_teams

        self._apply_distribution(distribution, users)
        return users.teams


class RandomMatcher(Matcher):
    """
    Distributes the players randomly to teams.
    """

    def distribute(self, num_teams: int, team_size: int, users: UserList) -> list[Team]:
        """
        For given parameter distributes the players to teams.
        :return: None
        :rtype: None
        """
        players = users.players
        teams: list = list(range(0, team_size)) * num_teams
        distribution: Distribution = Distribution()
        for player_index in range(len(players)):
            team_id = random.choice(teams)  # nosec random
            teams.remove(team_id)
            distribution.add(DistributionEntry(player_index=player_index, team_id=team_id))

        self._apply_distribution(distribution, users)

        return users.teams
