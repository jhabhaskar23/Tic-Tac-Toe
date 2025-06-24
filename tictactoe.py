# Tic-Tac-Toe Player:

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    # Return the Current Player:
    countX = sum(row.count(X) for row in board)
    countO = sum(row.count(O) for row in board)

    if countX <= countO:
        return X
    else:
        return O


def actions(board):

    # Determines all possible Actions to choose from:
    possibility = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possibility.add((i,j))
    return possibility


def result(board, action):

    # Provides Result of the actions on given State:
    i,j = action
    if board[i][j] is not None:
        raise ValueError("Invalid Action! Cell isn't EMPTY!")
    
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board

def winner(board):

    # Check for Rows and Columns:
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # Check for Diagonals:
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] is not None:
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] is not None:
        return board[1][1]
    
    return None

def terminal(board):
    
    # Checking if the game has already finished:
    if winner(board) is not None:
        return True
    
    elif sum(row.count(EMPTY) for row in board) == 0:
        return True
        
    return False


def utility(board):

    # Assigning utility points based on Result:
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    
    if terminal(board):
        return None

    current = player(board)
    best_move = None

    # Minimax Implementation using Alpha-Beta Pruning:
    if current == X:
        value = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        for action in actions(board):
            score = min_value(result(board, action), alpha, beta)
            if score > value:
                value = score
                best_move = action
                alpha = max(alpha, value)
    else:
        value = float('inf')
        alpha = float('-inf')
        beta = float('inf')
        for action in actions(board):
            score = max_value(result(board, action), alpha, beta)
            if score < value:
                value = score
                best_move = action
                beta = min(beta, value)

    return best_move


# Maximising the Utility for X: (Utility(X wins)=1)
def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v

# Minimising the Utility for O: (Utility(O Wins)=-1)
def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v

# Thanking You! It was a Nice Project!