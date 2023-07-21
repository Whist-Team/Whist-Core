from unittest.mock import patch, MagicMock

from tests.whist_core.player_table_base_test_case import PlayerAtTableBaseTestCase
from whist_core.cards.card import Card, Suit, Rank
from whist_core.cards.card_container import UnorderedCardContainer
from whist_core.game.errors import HandDoneError
from whist_core.game.hand import Hand
from whist_core.game.trick import Trick


class HandTestCase(PlayerAtTableBaseTestCase):
    def setUp(self):
        super().setUp()
        self.hand = Hand.deal(play_order=self.play_order)

    def test_first_trick(self):
        for i in range(len(self.player_order)):
            player = self.play_order.get_next_player()
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(self.hand.current_trick, Trick)

    def test_done_trick(self):
        first_trick = self.hand.current_trick
        # deliberately ignore illegal moves
        with patch('whist_core.game.legal_checker.LegalChecker.check_legal', return_value=True):
            while not first_trick.done:
                player = self.play_order.get_next_player()
                card = list(player.hand)[0]
                first_trick.play_card(player, card)
        next_trick = self.hand.next_trick(self.play_order)
        i = 0
        while i < len(self.player_order):
            i += 1
            player = self.play_order.get_next_player()
            self.assertEqual(12, len(player.hand))
        self.assertNotEqual(first_trick, next_trick)

    def test_second_card_same_suit(self):
        trick = self.hand.current_trick
        first_card = Card(suit=Suit.CLUBS, rank=Rank.A)
        second_card = Card(suit=Suit.CLUBS, rank=Rank.K)
        first_player = list(self.play_order)[0]
        self._enforce_card_in_hand(first_card, first_player)
        second_player = list(self.play_order)[1]
        self._enforce_card_in_hand(second_card, second_player)
        trick.play_card(first_player, first_card)
        trick.play_card(second_player, second_card)

    def test_json_after_play(self):
        first_player = list(self.play_order)[0]
        first_card = list(first_player.hand)[0]
        self.hand.current_trick.play_card(first_player, first_card)
        self.assertIsInstance(self.hand.json(), str)

    def test_hand_is_done_after_all_tricks(self):
        self.hand.tricks = [MagicMock] * 13
        with self.assertRaises(HandDoneError):
            self.hand.next_trick(self.play_order)

    def test_trump_is_string(self):
        model_dump = self.hand.model_dump()
        self.assertIsInstance(model_dump['trump'], str)

    def _enforce_card_in_hand(self, card, player):
        # Enforce card is in player's hand
        cards = list(player.hand.cards)
        cards[0] = card
        player.hand = UnorderedCardContainer.with_cards(cards)
