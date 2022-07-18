from unittest.mock import patch, MagicMock, PropertyMock

from tests.whist_core.team_base_test_case import TeamBaseTestCase
from whist_core.game.errors import GameNotStartedError, GameNotDoneError
from whist_core.game.rubber import Rubber
from whist_core.session.userlist import UserList


class RubberTestCase(TeamBaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.rubber = Rubber(teams=[self.team_a, self.team_b])

    def test_not_done(self):
        self.assertFalse(self.rubber.done)

    def test_game_not_started(self):
        with self.assertRaises(GameNotStartedError):
            self.rubber.current_game()

    def test_game_done_warning(self):
        with self.assertRaises(GameNotStartedError):
            with patch('whist_core.game.game.Game.done',
                       new_callable=MagicMock(return_value=True)):
                self.rubber.current_game()

    def test_next_game_not_done(self):
        self.rubber.next_game()
        with self.assertRaises(GameNotDoneError):
            self.rubber.next_game()

    def test_done(self):
        with patch('whist_core.game.rubber.Rubber.games_played', PropertyMock(return_value=3)):
            self.assertTrue(self.rubber.done)

    def test_create_random(self):
        players = [self.player_a, self.player_b, self.player_c, self.player_d]
        user_list = UserList()
        for player in players:
            user_list.append(player)
        rubber = Rubber.create_random(user_list, 2, 2)

        self.assertEqual(2, len(rubber.teams))
        self.assertEqual(2, len(rubber.teams[0].players))
        self.assertEqual(2, len(rubber.teams[1].players))
        self.assertNotIn(rubber.teams[0].players[0], rubber.teams[1].players)
        self.assertNotIn(rubber.teams[0].players[1], rubber.teams[1].players)
