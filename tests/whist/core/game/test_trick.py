from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.cards.card import Suit, Card, Rank
from whist.core.game.errors import TrickDoneError, NotPlayersTurnError
from whist.core.game.trick import Trick
from whist.core.game.warnings import TrickNotDoneWarning


class TrickTestCase(TeamBaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.play_order = [cls.player_a, cls.player_c, cls.player_b, cls.player_d]

    def setUp(self) -> None:
        self.trick = Trick(play_order=self.play_order, trump=Suit.CLUBS)

    def test_not_done(self):
        self.assertFalse(self.trick.done)

    def test_done(self):
        self._play_four_cards()

        self.assertTrue(self.trick.done)

    def test_winner(self):
        self._play_four_cards()

        self.assertEqual(self.play_order[0], self.trick.winner)

    def test_winner_not_done(self):
        with self.assertRaises(TrickNotDoneWarning):
            _ = self.trick.winner

    def test_play_card_done(self):
        self._play_four_cards()
        ace_spades = Card(Suit.SPADES, Rank.A)
        with self.assertRaises(TrickDoneError):
            self.trick.play_card(self.player_a, ace_spades)

    def test_not_turn(self):
        ace_spades = Card(Suit.SPADES, Rank.A)
        with self.assertRaises(NotPlayersTurnError):
            self.trick.play_card(self.player_b, ace_spades)

    def _play_four_cards(self):
        ace_heart = Card(Suit.HEARTS, Rank.A)
        king_heart = Card(Suit.HEARTS, Rank.K)
        queen_heart = Card(Suit.HEARTS, Rank.Q)
        jack_heart = Card(Suit.HEARTS, Rank.J)
        cards = [ace_heart, king_heart, queen_heart, jack_heart]
        for card, player in zip(cards, self.play_order):
            self.trick.play_card(player, card)
