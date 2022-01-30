import json
from unittest.mock import patch, MagicMock, PropertyMock

from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.cards.card import Card, Suit, Rank
from whist.core.game.game import Game
from whist.core.game.hand import Hand
from whist.core.game.play_order import PlayOrder
from whist.core.game.trick import Trick


class GameTestCase(TeamBaseTestCase):
    def setUp(self):
        super().setUp()
        self.game = Game(play_order=PlayOrder.from_team_list([self.team_a, self.team_b]))

    def test_first_hand(self):
        current_hand = self.game.next_hand()
        self.assertIsInstance(current_hand, Hand)

    def test_second_hand(self):
        first_hand = self.game.next_hand()
        first_hand.deal(self.game.play_order)
        first_hand.tricks = [PropertyMock(winner=self.game.play_order.play_order[0])] * 13
        second_hand = self.game.next_hand()
        self.assertNotEqual(first_hand, second_hand)

    def test_score_updated(self):
        first_hand = self.game.next_hand()
        first_hand.deal(self.game.play_order)
        first_hand.tricks = [PropertyMock(winner=self.game.play_order.play_order[0])] * 13
        _ = self.game.next_hand()
        self.assertEqual(7, self.game.score_card.score(self.team_a))
        self.assertEqual(0, self.game.score_card.score(self.team_b))

    def test_hand_not_done(self):
        first_hand = self.game.next_hand()
        with patch('whist.core.game.hand.Hand.done',
                   return_value=False):
            second_hand = self.game.next_hand()
        self.assertEqual(first_hand, second_hand)

    def test_done(self):
        with patch('whist.core.scoring.score_card.ScoreCard.max',
                   new_callable=MagicMock(return_value=4)):
            self.assertTrue(self.game.done)

    def test_not_done(self):
        self.assertFalse(self.game.done)

    def test_player_to_table_player(self):
        player_at_table = self.game.get_player(self.player_a)
        self.assertEqual(self.player_a, player_at_table.player)

    def test_trick_initialize(self):
        trick = self.game.current_trick
        for player in self.game.play_order:
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(trick, Trick)

    def test_trick_getter(self):
        hand = self.game.next_hand()
        first_trick = self.game.current_trick
        trick = hand.current_trick
        for player in self.game.play_order:
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(trick, Trick)
        self.assertEqual(first_trick, trick)

    def test_json_after_play(self):
        hand = self.game.next_hand()
        trick = hand.deal(self.game.play_order)
        first_card = Card(suit=Suit.CLUBS, rank=Rank.A)
        first_player = list(self.game.play_order)[0]
        trick.play_card(first_player, first_card)
        game_json = self.game.json()
        self.assertIsInstance(game_json, str)
        self.assertEqual(self.game, Game(**json.loads(game_json)))
