from tests.whist.core.player_table_base_test_case import PlayerAtTableBaseTestCase
from whist.core.cards.card import Suit, Card, Rank
from whist.core.cards.stack import Stack
from whist.core.game.errors import TrickDoneError, NotPlayersTurnError
from whist.core.game.trick import Trick
from whist.core.game.warnings import TrickNotDoneWarning


class TrickTestCase(PlayerAtTableBaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.trick = Trick(play_order=self.player_order, trump=Suit.CLUBS)

    def test_not_done(self):
        self.assertFalse(self.trick.done)

    def test_done(self):
        self._play_four_cards()

        self.assertTrue(self.trick.done)

    def test_winner(self):
        self._play_four_cards()

        self.assertEqual(self.player_order[0], self.trick.winner)

    def test_winner_not_done(self):
        with self.assertRaises(TrickNotDoneWarning):
            _ = self.trick.winner

    def test_play_card_done(self):
        self._play_four_cards()
        ace_spades = Card(suit=Suit.SPADES, rank=Rank.A)
        with self.assertRaises(TrickDoneError):
            self.trick.play_card(self.player_a, ace_spades)

    def test_not_turn(self):
        ace_spades = Card(suit=Suit.SPADES, rank=Rank.A)
        with self.assertRaises(NotPlayersTurnError):
            self.trick.play_card(self.player_order[1], ace_spades)

    def test_stack(self):
        ace_spades = Card(suit=Suit.SPADES, rank=Rank.A)
        self.trick.play_card(self.player_order[0], ace_spades)
        expected_stack = Stack()
        expected_stack.add(ace_spades)
        self.assertEqual(expected_stack, self.trick.stack)

    def _play_four_cards(self):
        ace_heart = Card(suit=Suit.HEARTS, rank=Rank.A)
        king_heart = Card(suit=Suit.HEARTS, rank=Rank.K)
        queen_heart = Card(suit=Suit.HEARTS, rank=Rank.Q)
        jack_heart = Card(suit=Suit.HEARTS, rank=Rank.J)
        cards = [ace_heart, king_heart, queen_heart, jack_heart]
        for card, player in zip(cards, self.player_order):
            self.trick.play_card(player, card)
