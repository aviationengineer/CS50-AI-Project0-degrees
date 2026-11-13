"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # X always moves first, so equal move counts mean it is X's turn.
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # A move is just the (row, column) of an empty square.
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    # Minimax explores lots of possible moves, so leave the input board alone.
    new_board = deepcopy(board)
    i, j = action
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check the rows, columns, and both diagonals for three matching marks.
    lines = [*board,
             *[[board[i][j] for i in range(3)] for j in range(3)],
             [board[i][i] for i in range(3)],
             [board[i][2 - i] for i in range(3)]]
    for line in lines:
        if line[0] is not EMPTY and line[0] == line[1] == line[2]:
            return line[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # The game ends with a win or when there are no empty squares left.
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # X is the maximizing player; O is the minimizing player.
    game_winner = winner(board)
    if game_winner == X:
        return 1
    if game_winner == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # Look ahead assuming X picks the highest score and O picks the lowest.
    def max_value(state):
        if terminal(state):
            return utility(state)
        value = -math.inf
        for action in actions(state):
            value = max(value, min_value(result(state, action)))
        return value

    def min_value(state):
        if terminal(state):
            return utility(state)
        value = math.inf
        for action in actions(state):
            value = min(value, max_value(result(state, action)))
        return value

    if player(board) == X:
        # X chooses the move with the best outcome it can force.
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value, best_action = value, action
    else:
        # O chooses the move that gives X the lowest possible score.
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value, best_action = value, action
    return best_action
