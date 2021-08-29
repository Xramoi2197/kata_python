def is_solved(board):
    lines = board
    for i in range(0, 3):
        lines.append([board[0][i], board[1][i], board[2][i]])
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[2][0], board[1][1], board[0][2]])
    win_list = []
    for line in lines:
        win_list.append(is_win(line))
    if 1 in win_list:
        return 1
    elif 2 in win_list:
        return 2
    elif -1 in win_list:
        return -1
    return 0


def is_win(line):
    win = set(line)
    if len(win) == 1:
        return line[0]
    elif 0 in win:
        return -1
    return 0
