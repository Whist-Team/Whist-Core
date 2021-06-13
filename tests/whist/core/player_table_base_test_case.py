from tests.whist.core.team_base_test_case import TeamBaseTestCase
from whist.core.cards.hand import Hand
from whist.core.game.player_at_table import PlayerAtTable


class PlayerAtTableBaseTestCase(TeamBaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.play_order: list[PlayerAtTable] = [PlayerAtTable(cls.player_a, Hand.empty()),
                                               PlayerAtTable(cls.player_c, Hand.empty()),
                                               PlayerAtTable(cls.player_b, Hand.empty()),
                                               PlayerAtTable(cls.player_d, Hand.empty())]
