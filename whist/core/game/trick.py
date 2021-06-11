from pydantic import BaseModel

from whist.core.cards.card import Card, Suit
from whist.core.cards.stack import Stack
from whist.core.game.errors import NotPlayersTurnError
from whist.core.game.warnings import TrickNotDoneWarning
from whist.core.user.player import Player


class Trick(BaseModel):
    play_order: list[Player] = []
    stack: Stack = Stack()
    trump: Suit = None

    @property
    def done(self):
        return len(self.stack) == len(self.play_order)

    @property
    def winner(self) -> Player:
        if not self.done:
            raise TrickNotDoneWarning()
        winner_card = self.stack.winner_card(self.trump)
        return self.play_order[self.stack.get_turn(winner_card)]

    def play_card(self, player: Player, card: Card) -> None:
        turn = len(self.stack)
        if player is not self.play_order[turn]:
            raise NotPlayersTurnError(player, self.play_order[turn])
        self.stack.add(card)
