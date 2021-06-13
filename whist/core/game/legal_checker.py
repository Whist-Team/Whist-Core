from whist.core.cards.card import Card
from whist.core.cards.hand import Hand


class LegalChecker:
    @staticmethod
    def check_legal(hand: Hand, lead: Card) -> bool:
        first_card_played = lead is not None
        return not (first_card_played and hand.contain_suit(lead.suit))
