from whist.core.cards.card import Card, Suit
from whist.core.cards.stack import Stack
from whist.core.game.errors import NotPlayersTurnError, TrickDoneError
from whist.core.game.warnings import TrickNotDoneWarning
from whist.core.user.player import Player


class Trick:

    def __init__(self, play_order: list[Player], trump: Suit):
        self._play_order = play_order
        self._stack: Stack = Stack()
        self._trump = trump

    @property
    def done(self):
        return len(self._stack) == len(self._play_order)

    @property
    def winner(self) -> Player:
        if not self.done:
            raise TrickNotDoneWarning()
        winner_card = self._stack.winner_card(self._trump)
        return self._play_order[self._stack.get_turn(winner_card)]

    def play_card(self, player: Player, card: Card) -> None:
        turn = len(self._stack)
        if turn == len(self._play_order):
            raise TrickDoneError()
        if player != self._play_order[turn]:
            raise NotPlayersTurnError(player, self._play_order[turn])
        self._stack.add(card)
