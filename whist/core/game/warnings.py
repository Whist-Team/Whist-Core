"""Warnings during game phase."""


class GameDoneWarning(Warning):
    """Is raised when some requests action on a Game already done."""


class TrickNotDoneWarning(Warning):
    """The current trick is not done yet."""


class ServSuitFirstWarning(Warning):
    """Player must serv the suit of the lead."""
