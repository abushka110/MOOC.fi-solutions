class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')

# solution
def most_goals(players_list):
    def get_goals_num(player: BallPlayer):
        return player.goals

    # sort list of players and return last player's (player with the highest goals count) name
    return sorted(players_list, key=get_goals_num)[-1].name

def most_points(players_list):
    def get_points_num(player: BallPlayer):
        return player.goals + player.passes

    # sort players by points count and [-1] return the last element
    player_with_most_points = sorted(players_list, key=get_points_num)[-1]

    # return name and number of player with the most points
    return (player_with_most_points.name, player_with_most_points.number)

def least_minutes(players_list):
    def get_minutes(player: BallPlayer):
        return player.minutes

    return sorted(players_list, key=get_minutes)[0]

# test
if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))

    # expected output:
    # Archie Bonkers
    # ('Cruella De Hill', 9)
    # BallPlayer(name=Donald Quack, number=4, goals=3, assists=9, minutes=12)
