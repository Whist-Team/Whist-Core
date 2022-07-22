def get_players_by_team(play_order):
    players_by_team = [[], []]
    for player in play_order:
        players_by_team[player.team].append(player.player)
    return players_by_team
