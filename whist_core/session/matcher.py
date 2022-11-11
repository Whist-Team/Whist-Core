"""
Match making tool.
"""
import abc
import random
from itertools import permutations
from typing import Any

from pydantic import BaseModel

from whist_core.error.matcher_error import NotEnoughPlayersError
from whist_core.session.distribution import Distribution, DistributionEntry
from whist_core.session.userlist import UserList

subclass_registry = {}


# pylint: disable=too-few-public-methods
class Matcher(abc.ABC, BaseModel):
    """
    Abstrakt class for player to teams matching.
    """
    teams: list[Distribution] = []
    number_teams: int
    team_size: int

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        subclass_registry[cls.__name__] = cls

    class Config:
        extra = "allow"

    @abc.abstractmethod
    def distribute(self, users: UserList) -> Distribution:
        """
        Distributes cards according to subclass implementation.
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

    def _apply_distribution(self, distribution):
        self.teams.append(distribution)


class RoundRobinMatcher(Matcher):
    """
    Distributes the players in the order of the user list.
    """
    iteration: int = 0
    distributions: list[Distribution] = []

    def __init__(self, number_teams: int, team_size: int, **data):
        super().__init__(number_teams=number_teams, team_size=team_size, **data)
        number_players = self.team_size * self.number_teams

        if len(self.distributions) == 0:
            for distribution_int in sorted(
                    set(permutations((x % self.number_teams for x in range(number_players))))):
                distribution = Distribution()
                for player_index, team_id in enumerate(distribution_int):
                    distribution.add(DistributionEntry(player_index=player_index, team_id=team_id))
                self.distributions.append(distribution)

    def distribute(self, users: UserList) -> Distribution:
        """
        Distributes one player to each team each round in order of the user list. Repeats until
        the user list is empty.
        :param users: the players to be distributed to teams
        :return: the teams in round robin distribution
        """
        distribution = self.distributions[self.iteration]
        self.iteration += 1
        self._apply_distribution(distribution)

        return distribution


class RandomMatcher(Matcher):
    """
    Distributes the players randomly to teams.
    """

    def distribute(self, users: UserList) -> Distribution:
        """
        For given parameter distributes the players to teams.
        :return: None
        :rtype: None
        """
        players = users.players
        if len(players) != self.number_teams * self.team_size:
            raise NotEnoughPlayersError()
        teams: list = list(range(0, self.team_size)) * self.number_teams
        distribution: Distribution = Distribution()
        for player_index in range(len(players)):
            team_id = random.choice(teams)  # nosec random
            teams.remove(team_id)
            distribution.add(DistributionEntry(player_index=player_index, team_id=team_id))

        self._apply_distribution(distribution)

        return distribution
