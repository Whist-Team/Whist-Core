from tests.whist_core.player_table_base_test_case import PlayerAtTableBaseTestCase
from whist_core.cards.card import Suit, Card, Rank

from whist_core.cards.card_container import OrderedCardContainer
from whist_core.game.errors import TrickDoneError, NotPlayersTurnError, CardNotInHandError
from whist_core.game.trick import Trick
from whist_core.game.warnings import TrickNotDoneWarning


class TrickTestCase(PlayerAtTableBaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.trick = Trick(play_order=self.player_order, stack=OrderedCardContainer.empty(),
                           trump=Suit.CLUBS)

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

    def test_card_remove(self):
        ace_spades = Card(suit=Suit.SPADES, rank=Rank.A)
        player = self.player_order[0]
        player.hand.add(ace_spades)
        self.trick.play_card(player, ace_spades)
        self.assertNotIn(ace_spades, player.hand)

    def test_not_turn(self):
        ace_spades = Card(suit=Suit.SPADES, rank=Rank.A)
        with self.assertRaises(NotPlayersTurnError):
            self.trick.play_card(self.player_order[1], ace_spades)

    def test_card_not_in_hand(self):
        player = list(self.player_order)[0]
        with self.assertRaises(CardNotInHandError):
            self.trick.play_card(player, Card(suit=Suit.SPADES, rank=Rank.A))

    def test_stack(self):
        ace_spades = Card(suit=Suit.SPADES, rank=Rank.A)
        player = self.player_order[0]
        player.hand.add(ace_spades)
        self.trick.play_card(player, ace_spades)
        expected_stack = OrderedCardContainer.empty()
        expected_stack.add(ace_spades)
        self.assertEqual(expected_stack, self.trick.stack)

    def test_trick_json_after_player(self):
        ace_spades = Card(suit=Suit.SPADES, rank=Rank.A)
        player = self.player_order[0]
        player.hand.add(ace_spades)
        self.trick.play_card(player, ace_spades)
        trick_json = self.trick.json()
        self.assertIsInstance(trick_json, str)

    def test_dict_trump(self):
        self.assertEqual({'trump': 'clubs'}, self.trick.dict(include={'trump'}))

    def _play_four_cards(self):
        ace_heart = Card(suit=Suit.HEARTS, rank=Rank.A)
        king_heart = Card(suit=Suit.HEARTS, rank=Rank.K)
        queen_heart = Card(suit=Suit.HEARTS, rank=Rank.Q)
        jack_heart = Card(suit=Suit.HEARTS, rank=Rank.J)
        cards = [ace_heart, king_heart, queen_heart, jack_heart]
        for card, player in zip(cards, self.player_order):
            player.hand.add(card)
            self.trick.play_card(player, card)
