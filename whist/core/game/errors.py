from whist.core.user.player import Player


class NotPlayersTurnError(Exception):
    def __init__(self, player: Player, turn_player: Player):
        super().__init__()
        self.message = f'Is not {player} turn, but {turn_player}.'


class NoTrumpSelectedError(Exception):
    pass


class TrickDoneError(Exception):
    pass
