from whist_core.scoring.score import Score
from whist_core.scoring.team import Team


class ScoreCalculator:
    @staticmethod
    def calc_score(current_hand, play_order):
        tricks_won = [0, 0]
        for trick in current_hand.tricks:
            winner = trick.winner
            tricks_won[winner.team] += 1
        tricks_won = [max(0, trick_score - 6) for trick_score in tricks_won]
        players_by_team = [[], []]
        for player in play_order:
            players_by_team[player.team].append(player.player)
        teams = [Team(players=players) for players in players_by_team]
        score = Score(teams=teams, scores=tricks_won)
        return score
