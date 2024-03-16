# solution
from random import choice

def dices(die_type: str):
    if die_type == "A":
        return [3, 3, 3, 3, 3, 6]
    elif die_type == "B":
        return [2, 2, 2, 5, 5, 5]
    elif die_type == "C":
        return [1, 4, 4, 4, 4, 4]
    
def roll(die: str):
    die_list = dices(die)
    num = choice(die_list)
    return num

def play(die1: str, die2: str, times: int):
    first_won = 0
    second_won = 0
    ties = 0
    for i in range(times):
        player_one_throw = roll(die1)
        player_two_throw = roll(die2)
        if player_one_throw > player_two_throw:
            first_won += 1
        elif player_one_throw < player_two_throw:
            second_won += 1
        else:
            ties += 1
    return first_won, second_won, ties

# test
if __name__ == "__main__":
    # test 1
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    # test 2
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)