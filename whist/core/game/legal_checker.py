from whist.core.cards.card import Card
from whist.core.cards.hand import Hand
from whist.core.game.warnings import ServSuitFirstWarning


class LegalChecker:
    @staticmethod
    def check_legal(hand: Hand, lead: Card) -> None:
        if lead is not None and hand.contain_suit(lead.suit):
            raise ServSuitFirstWarning()
