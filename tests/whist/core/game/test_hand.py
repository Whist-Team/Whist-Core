from tests.whist.core.player_table_base_test_case import PlayerAtTableBaseTestCase
from whist.core.cards.card import Suit
from whist.core.game.hand import Hand
from whist.core.game.trick import Trick
from whist.core.game.warnings import TrickNotDoneWarning


class HandTestCase(PlayerAtTableBaseTestCase):
    def setUp(self):
        super().setUp()
        self.hand = Hand(self.play_order, Suit.HEARTS)

    def test_first_trick(self):
        first_trick = self.hand.deal()
        for player in self.play_order:
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(first_trick, Trick)

    def test_not_done_trick(self):
        _ = self.hand.deal()
        with self.assertRaises(TrickNotDoneWarning):
            _ = self.hand.next_trick()
