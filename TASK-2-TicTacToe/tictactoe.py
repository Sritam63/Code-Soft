import math
from copy import deepcopy
import numpy as np

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def get_diagonal(board):
    return [[board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]]

def get_columns(board):
    columns = []
    for i in range(3):
        columns.append([row[i] for row in board])
    return columns

def three_in_a_row(row):
    return row[0] is not None and row.count(row[0]) == 3

def player(board):
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    return O if count_x > count_o else X

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    i, j = action
    if board[i][j] is not EMPTY:
        raise Exception("Invalid move")
    next_move = player(board)
    new_board = deepcopy(board)
    new_board[i][j] = next_move
    return new_board

def winner(board):
    rows = board + get_diagonal(board) + get_columns(board)
    for row in rows:
        if three_in_a_row(row):
            return row[0]
    return None

def terminal(board):
    return winner(board) is not None or all(all(cell is not EMPTY for cell in row) for row in board)

def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0

def max_alpha_beta_pruning(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    max_val = float("-inf")
    best_action = None
    for action in actions(board):
        min_val, _ = min_alpha_beta_pruning(result(board, action), alpha, beta)
        if min_val > max_val:
            max_val = min_val
            best_action = action
        alpha = max(alpha, max_val)
        if beta <= alpha:
            break
    return max_val, best_action

def min_alpha_beta_pruning(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    min_val = float("inf")
    best_action = None
    for action in actions(board):
        max_val, _ = max_alpha_beta_pruning(result(board, action), alpha, beta)
        if max_val < min_val:
            min_val = max_val
            best_action = action
        beta = min(beta, min_val)
        if beta <= alpha:
            break
    return min_val, best_action

def minimax(board):
    if terminal(board):
        return None
    current_player = player(board)
    if current_player == X:
        _, action = max_alpha_beta_pruning(board, float("-inf"), float("inf"))
    else:
        _, action = min_alpha_beta_pruning(board, float("-inf"), float("inf"))
    return action
