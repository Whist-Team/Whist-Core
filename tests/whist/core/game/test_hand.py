from unittest.mock import patch

from tests.whist.core.player_table_base_test_case import PlayerAtTableBaseTestCase
from whist.core.cards.card import Card, Suit, Rank
from whist.core.error.hand_error import HandAlreadyDealtError
from whist.core.game.hand import Hand
from whist.core.game.trick import Trick
from whist.core.game.warnings import TrickNotDoneWarning


class HandTestCase(PlayerAtTableBaseTestCase):
    def setUp(self):
        super().setUp()
        self.hand = Hand()

    def test_first_trick(self):
        first_trick = self.hand.deal(self.play_order)
        for i in range(len(self.player_order)):
            player = self.play_order.next_player()
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(first_trick, Trick)

    def test_done_trick(self):
        first_trick = self.hand.deal(self.play_order)
        # deliberately ignore illegal moves
        with patch('whist.core.game.legal_checker.LegalChecker.check_legal', return_value=True):
            while not first_trick.done:
                player = self.play_order.next_player()
                card = player.hand.pop_random()
                first_trick.play_card(player, card)
        next_trick = self.hand.next_trick(self.play_order)
        i = 0
        while i < len(self.player_order):
            i += 1
            player = self.play_order.next_player()
            self.assertEqual(12, len(player.hand))
        self.assertNotEqual(first_trick, next_trick)

    def test_not_done_trick(self):
        _ = self.hand.deal(self.play_order)
        with self.assertRaises(TrickNotDoneWarning):
            _ = self.hand.next_trick(self.play_order)

    def test_trick_getter(self):
        first_trick = self.hand.deal(self.play_order)
        trick = self.hand.current_trick
        for player in self.play_order:
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(trick, Trick)
        self.assertEqual(first_trick, trick)

    def test_safe_deal(self):
        _ = self.hand.deal(self.play_order)
        with self.assertRaises(HandAlreadyDealtError):
            self.hand.deal(self.play_order)

    def test_trick_initialized(self):
        with self.assertRaises(IndexError):
            _ = self.hand.current_trick

    def test_second_card_same_suit(self):
        trick = self.hand.deal(self.play_order)
        first_card = Card(suit=Suit.CLUBS, rank=Rank.A)
        second_card = Card(suit=Suit.CLUBS, rank=Rank.K)
        first_player = list(self.play_order)[0]
        second_player = list(self.play_order)[1]
        trick.play_card(first_player, first_card)
        trick.play_card(second_player, second_card)

    def test_play_order_untouched(self):
        ace = Card(rank=Rank.A, suit=Suit.CLUBS)
        king = Card(rank=Rank.K, suit=Suit.CLUBS)
        queen = Card(rank=Rank.Q, suit=Suit.CLUBS)
        jack = Card(rank=Rank.J, suit=Suit.CLUBS)
        trick = self.hand.deal(self.play_order)
        trick.play_card(list(self.play_order)[0], queen)
        trick.play_card(list(self.play_order)[1], jack)
        trick.play_card(list(self.play_order)[2], ace)
        trick.play_card(list(self.play_order)[3], king)
        next_trick = self.hand.next_trick(self.play_order)
        self.assertEqual(list(next_trick.play_order)[0].player, self.player_b)

    def test_json_after_play(self):
        trick = self.hand.deal(self.play_order)
        first_card = Card(suit=Suit.CLUBS, rank=Rank.A)
        first_player = list(self.play_order)[0]
        trick.play_card(first_player, first_card)
        self.assertIsInstance(self.hand.json(), str)
