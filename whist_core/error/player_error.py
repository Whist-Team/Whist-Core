"""Exceptions that occur in player or user"""


class NegativeRatingError(Exception):
    """
    Will be raised if a attempt to assign a negative rating to a player"""
