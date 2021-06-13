from tests.whist.core.player_table_base_test_case import PlayerAtTableBaseTestCase
from whist.core.cards.card import Suit
from whist.core.game.hand import Hand
from whist.core.game.trick import Trick


class HandTestCase(PlayerAtTableBaseTestCase):
    def test_next_trick(self):
        hand = Hand(self.play_order, Suit.HEARTS)
        first_trick = hand.deal()
        for player in self.play_order:
            self.assertEqual(13, len(player.hand))
        self.assertIsInstance(first_trick, Trick)
