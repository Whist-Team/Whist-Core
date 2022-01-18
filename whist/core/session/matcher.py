"""
Match making tool.
"""
import abc
import random

from whist.core.scoring.team import Team
from whist.core.session.userlist import UserList


# pylint: disable=too-few-public-methods
class Matcher(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def distribute(num_teams: int, team_size: int, users: UserList) -> list[Team]:
        """
        Distributes cards according to subclass implementation.
        :param num_teams: the amount of teams
        :param team_size: how many players per team
        :param users: the userlist at that table
        :return: the list of teams with players distributed to them
        """
        raise NotImplementedError


class RandomMatch(Matcher):
    """
    Distributes the players randomly to teams.
    """

    @staticmethod
    def distribute(num_teams: int, team_size: int, users: UserList) -> list[Team]:
        """
        For given parameter distributes the players to teams.
        :return: None
        :rtype: None
        """
        players = users.players
        teams: list = list(range(0, team_size)) * num_teams
        for player in players:
            team_id = random.choice(teams)
            users.change_team(player, team_id)
            teams.remove(team_id)
        return users.teams
