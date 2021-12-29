"""Errors regarding table logic."""


class TableFullError(Exception):
    """
    Thrown if the table is already full.
    """


class TeamFullError(Exception):
    """
    Thrown if the team is already full.
    """


class PlayerNotJoinedError(Exception):
    """
    Raised if a player has not yet joined the table.
    """
