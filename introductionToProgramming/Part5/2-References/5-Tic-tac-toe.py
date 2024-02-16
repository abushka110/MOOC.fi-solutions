# solution
def play_turn(game_board: list, x: int, y: int, piece: str):
    xy_allowed = [0, 1, 2]
    if x not in xy_allowed or y not in xy_allowed:
        return False
    if game_board[y][x] == '':
        game_board[y][x] = piece
        return True
    return False

# test
if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board) # true