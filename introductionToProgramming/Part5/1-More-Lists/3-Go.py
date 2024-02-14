# solution
def who_won(game_board: list):
    player_one_points = 0
    player_two_points = 0
    for lines in game_board:
        for pieces in lines:
            if pieces == 1:
                player_one_points += 1
            elif pieces == 2:
                player_two_points += 1
    if player_one_points > player_two_points:
        return 1
    elif player_one_points < player_two_points:
        return 2
    else:
        return 0