# A computer that plays Tic Tac Toe perfectly
# Uses the Minimax algorithm with alpha beta pruning

from TTTGame import Game
import random

# Given a game object, returns the integer corresponding to the
#   square of the best move by calling the recursive minimax func
def getMove(game):
    value = -1000
    best = -1
    moves = []

    # Find availible moves
    for x in range(9):
        if game.board[x] == " ": moves.append(x)
    random.shuffle(moves)

    # Computes the move with the best score
    for i in moves:
        g1 = game.copy()
        g1.player(i)
        result = -minmax(g1, -2, 2)
        if result > value: 
            value = result
            best = i
    return best

# Implementation of Minimax algorithm with alpha beta pruning
def minmax(game, alpha, beta):
    result = game.isOver()

    # If game is over, return score corresponding with who won
    if(result != " "):
        if result == game.currPlayer: return 1
        elif result == "Nobody": return 0
        else: return -1

    # else, recursively call minimax on each availible move
    bestVal = -2
    for move in range(9):
        g1 = game.copy()
        if g1.player(move):
            val = -1*minmax(g1, -1*beta, -1*alpha)
            bestVal = max(val, bestVal)
            alpha = max(alpha, bestVal)
        if alpha >= beta: break
    return bestVal
    