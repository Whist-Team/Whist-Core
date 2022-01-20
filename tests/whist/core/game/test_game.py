from unittest.mock import patch, PropertyMock

from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.game.game import Game
from whist.core.game.hand import Hand
from whist.core.game.trick import Trick


class GameTestCase(TeamBaseTestCase):
    def setUp(self):
        super().setUp()
        self.game = Game([self.team_a, self.team_b])

    def test_first_hand(self):
        current_hand = self.game.next_hand()
        self.assertIsInstance(current_hand, Hand)

    def test_second_hand(self):
        first_hand = self.game.next_hand()
        with patch('whist.core.game.hand.Hand.done', new_callable=PropertyMock(return_value=True)):
            second_hand = self.game.next_hand()
        self.assertNotEqual(first_hand, second_hand)

    def test_hand_not_done(self):
        first_hand = self.game.next_hand()
        with patch('whist.core.game.hand.Hand.done',
                   new_callable=PropertyMock(return_value=False)):
            second_hand = self.game.next_hand()
        self.assertEqual(first_hand, second_hand)

    def test_done(self):
        with patch('whist.core.scoring.score_card.ScoreCard.max',
                   new_callable=PropertyMock(return_value=4)):
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
