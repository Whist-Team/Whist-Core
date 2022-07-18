import json
from unittest.mock import patch, MagicMock

from tests.whist_core.team_base_test_case import TeamBaseTestCase
from whist_core.error.table_error import PlayerNotJoinedError
from whist_core.game.errors import HandNotDoneError
from whist_core.game.game import Game
from whist_core.game.hand import Hand
from whist_core.game.play_order import PlayOrder
from whist_core.game.trick import Trick
from whist_core.user.player import Player


class GameTestCase(TeamBaseTestCase):
    def setUp(self):
        super().setUp()
        self.game = Game(play_order=PlayOrder.from_team_list([self.team_a, self.team_b]))

    def test_first_hand(self):
        current_hand = self.game.next_hand()
        self.assertIsInstance(current_hand, Hand)

    def test_hand_not_done(self):
        _ = self.game.next_hand()
        with self.assertRaises(HandNotDoneError):
            self.game.next_hand()

    def test_done(self):
        with patch('whist_core.scoring.score_card.ScoreCard.max',
                   new_callable=MagicMock(return_value=4)):
            self.assertTrue(self.game.done)

    def test_not_done(self):
        self.assertFalse(self.game.done)

    def test_player_to_table_player(self):
        player_at_table = self.game.get_player(self.player_a)
        self.assertEqual(self.player_a, player_at_table.player)

    def test_player_not_joined(self):
        not_join_player = Player(user_id=6, username='not joined', rating=1700)
        with self.assertRaises(PlayerNotJoinedError):
            self.game.get_player(not_join_player)

    def test_trick_initialize(self):
        hand = self.game.next_hand()
        trick = hand.current_trick
        for player in self.game.play_order:
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(trick, Trick)

    def test_json_after_play(self):
        trick = self.game.next_hand().current_trick
        first_player = list(self.game.play_order)[0]
        first_card = list(first_player.hand)[0]
        trick.play_card(first_player, first_card)
        game_json = self.game.json()
        self.assertIsInstance(game_json, str)
        self.assertEqual(self.game, Game(**json.loads(game_json)))
