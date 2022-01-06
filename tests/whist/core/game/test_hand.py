from unittest.mock import patch

from tests.whist.core.player_table_base_test_case import PlayerAtTableBaseTestCase
from whist.core.error.hand_error import HandAlreadyDealtError
from whist.core.game.hand import Hand
from whist.core.game.trick import Trick
from whist.core.game.warnings import TrickNotDoneWarning


class HandTestCase(PlayerAtTableBaseTestCase):
    def setUp(self):
        super().setUp()
        self.hand = Hand(self.play_order)

    def test_first_trick(self):
        first_trick = self.hand.deal()
        i = 0
        while i < len(self.player_order):
            i += 1
            player = self.play_order.next_player()
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(first_trick, Trick)

    def test_done_trick(self):
        first_trick = self.hand.deal()
        # deliberately ignore illegal moves
        with patch('whist.core.game.legal_checker.LegalChecker.check_legal', return_value=True):
            while not first_trick.done:
                player = self.play_order.next_player()
                card = player.hand._cards.pop()
                first_trick.play_card(player, card)
        next_trick = self.hand.next_trick()
        i = 0
        while i < len(self.player_order):
            i += 1
            player = self.play_order.next_player()
            self.assertEqual(12, len(player.hand))
        self.assertNotEqual(first_trick, next_trick)

    def test_not_done_trick(self):
        _ = self.hand.deal()
        with self.assertRaises(TrickNotDoneWarning):
            _ = self.hand.next_trick()

    def test_player_to_table_player(self):
        player_at_table = self.hand.get_player(self.player_a)
        self.assertEqual(self.player_a, player_at_table.player)

    def test_trick_getter(self):
        first_trick = self.hand.deal()
        trick = self.hand.current_trick
        for player in self.play_order:
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(trick, Trick)
        self.assertEqual(first_trick, trick)

    def test_safe_deal(self):
        _ = self.hand.deal()
        with self.assertRaises(HandAlreadyDealtError):
            self.hand.deal()

    def test_trick_initialized(self):
        trick = self.hand.current_trick
        for player in self.play_order:
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(trick, Trick)
