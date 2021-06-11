from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.cards.card import Suit, Card, Rank
from whist.core.game.trick import Trick


class TrickTestCase(TeamBaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.play_order = [cls.player_a, cls.player_c, cls.player_b, cls.player_d]

    def test_not_done(self):
        trick = Trick(play_order=self.play_order, trump=Suit.SPADES)
        self.assertFalse(trick.done)

    def test_done(self):
        trick = Trick(play_order=self.play_order, trump=Suit.CLUBS)

        ace_heart = Card(Suit.HEARTS, Rank.A)
        king_heart = Card(Suit.HEARTS, Rank.K)
        queen_heart = Card(Suit.HEARTS, Rank.Q)
        jack_heart = Card(Suit.HEARTS, Rank.J)
        cards = [ace_heart, king_heart, queen_heart, jack_heart]
        for card, player in zip(cards, self.play_order):
            trick.play_card(player, card)

        self.assertTrue(trick.done)
