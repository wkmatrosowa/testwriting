import numpy as np


def is_solved(board):
    columns = np.transpose(np.array(board))
    columns = [list(column) for column in columns]
    diags = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    all_lines = board + columns + diags
    for line in all_lines:
        if line[0] == line[1] == line[2] and line[0] != 0:
            return line[0]
    if 0 in board[0] or 0 in board[1] or 0 in board[2]:
        return -1
    else:
        return 0
