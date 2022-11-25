import json
from unittest.mock import patch, MagicMock

from tests.whist_core.base_test_case import BaseTestCase
from whist_core.error.table_error import TeamFullError, TableFullError, TableNotReadyError, \
    TableNotStartedError, PlayerNotJoinedError, TableSettingsError
from whist_core.game.errors import RubberNotDoneError
from whist_core.game.rubber import Rubber
from whist_core.session.matcher import RandomMatcher, RoundRobinMatcher
from whist_core.session.table import Table
from whist_core.user.player import Player


class TableTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.mock_user_list = MagicMock()
        self.table = Table(name='test table', min_player=1, max_player=4,
                           matcher=RoundRobinMatcher(number_teams=2, team_size=2))

    def test_table_random_matcher_from_dict(self):
        self.table.matcher = RandomMatcher(number_teams=2, team_size=2)
        table_from_dict = Table(**self.table.dict())
        self.assertEqual(self.table, table_from_dict)
        self.assertIsInstance(table_from_dict.matcher, RandomMatcher)

    def test_table_random_matcher_from_dict_generic(self):
        self.table.matcher = RandomMatcher(number_teams=2, team_size=2)
        table_dict = dict(self.table)
        table_from_dict = Table(**table_dict)
        self.assertEqual(self.table, table_from_dict)
        self.assertIsInstance(table_from_dict.matcher, RandomMatcher)

    def test_table_random_matcher_from_json(self):
        self.table.matcher = RandomMatcher(number_teams=2, team_size=2)
        table_json = self.table.json()
        table_dict_from_json = json.loads(table_json)
        table_from_json = Table(**table_dict_from_json)
        self.assertEqual(self.table, table_from_json)
        self.assertIsInstance(table_from_json.matcher, RandomMatcher)

    def test_table_random_matcher_from_json_generic(self):
        self.table.matcher = RandomMatcher(number_teams=2, team_size=2)
        table_json = self.table.json()
        table_from_json = Table(**json.loads(table_json))
        self.assertEqual(self.table, table_from_json)
        self.assertIsInstance(table_from_json.matcher, RandomMatcher)

    def test_min_max_validation(self):
        with self.assertRaises(TableSettingsError):
            _ = Table(name='faulty table', min_player=3, max_player=2,
                      matcher=RandomMatcher(number_teams=2, team_size=2))

    def test_ready(self):
        self.table.join(self.player)
        self.table.player_ready(self.player)
        self.assertTrue(self.table.ready)

    def test_not_ready(self):
        self.table.join(self.player)
        self.table.player_ready(self.player)
        self.table.player_unready(self.player)
        self.assertFalse(self.table.ready)

    def test_not_ready_min_player(self):
        table = Table(name='test table', min_player=2, max_player=4,
                      matcher=RandomMatcher(number_teams=2, team_size=2))
        table.join(self.player)
        table.player_ready(self.player)
        self.assertFalse(table.ready)

    def test_ready_player_not_joined(self):
        with self.assertRaises(PlayerNotJoinedError):
            self.table.player_ready(self.player)

    def test_unready_player_not_joined(self):
        with self.assertRaises(PlayerNotJoinedError):
            self.table.player_unready(self.player)

    def test_join(self):
        self.table.join(self.player)
        self.assertEqual(1, len(self.table))

    def test_leave(self):
        self.table.join(self.player)
        self.table.leave(self.player)
        self.assertEqual(0, len(self.table))

    def test_join_full_team(self):
        self.table.team_size = 1
        player = Player(user_id=2, username='hank', rating=1)
        self.table.join(self.player)
        self.table.join_team(self.player, 1)
        with self.assertRaises(TeamFullError):
            self.table.join_team(player, 1)

    def test_join_full_table(self):
        self.table.max_player = 1
        player = Player(user_id=2, username='hank', rating=1)
        self.table.join(self.player)
        self.table.join_team(self.player, 1)
        with self.assertRaises(TableFullError):
            self.table.join(player)

    def test_conversion(self):
        self.table.join(self.player)
        table_dict = self.table.dict()
        table = Table(**table_dict)
        self.assertEqual(self.table, table)

    def test_start_random(self):
        self.table.matcher = RandomMatcher(number_teams=2, team_size=2)
        self._ready_four_players()
        self.table.start()
        self.assertTrue(self.table.started)
        self.assertIsInstance(self.table.current_rubber, Rubber)
        self.assertTrue(isinstance(self.table.matcher, RandomMatcher))

    def test_start_robin(self):
        self.table = Table(name='test table', min_player=1, max_player=4,
                           matcher=RoundRobinMatcher(number_teams=2, team_size=2))
        self._ready_four_players()
        self.table.start()
        self.assertTrue(self.table.started)
        self.assertIsInstance(self.table.current_rubber, Rubber)
        self.assertTrue(isinstance(self.table.matcher, RoundRobinMatcher))

    def test_start_early(self):
        self.table.join(self.player)
        self.table.player_ready(self.player)
        self.table.start()
        self.assertTrue(self.table.started)

    def test_not_ready_start(self):
        self.table.join(self.player)
        with self.assertRaises(TableNotReadyError):
            self.table.start()
        self.assertFalse(self.table.started)

    def test_rubber_without_start(self):
        with self.assertRaises(TableNotStartedError):
            _ = self.table.current_rubber

    def test_next_rubber(self):
        self._ready_four_players()
        self.table.start()
        with patch('whist_core.game.rubber.Rubber.done', return_value=True):
            self.table.next_rubber()
        self.assertEqual(2, len(self.table.rubbers))

    def test_next_rubber_not_done(self):
        self._ready_four_players()
        self.table.start()
        with self.assertRaises(RubberNotDoneError):
            self.table.next_rubber()
        self.assertEqual(1, len(self.table.rubbers))

    def test_next_rubber_first(self):
        self._ready_four_players()
        with self.assertRaises(TableNotStartedError):
            self.table.next_rubber()
        self.assertEqual(0, len(self.table.rubbers))

    def _ready_four_players(self):
        second_player = Player(username='miles', rating=3000)
        third_player = Player(username='nico', rating=300)
        forth_player = Player(username='abc', rating=200)
        self.table.join(self.player)
        self.table.join(second_player)
        self.table.join(third_player)
        self.table.join(forth_player)
        self.table.player_ready(self.player)
        self.table.player_ready(second_player)
        self.table.player_ready(third_player)
        self.table.player_ready(forth_player)
