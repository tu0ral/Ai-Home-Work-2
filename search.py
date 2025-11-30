from math import inf
from heuristic import evaluate


def minimax(game, board):
    def max_value(state):
        if game.terminal(state):
            return game.utility(state), None
        v = -inf
        best = None
        for a in sorted(game.actions(state)):
            val, _ = min_value(game.result(state, a))
            if val > v:
                v, best = val, a
        return v, best

    def min_value(state):
        if game.terminal(state):
            return game.utility(state), None
        v = +inf
        best = None
        for a in sorted(game.actions(state)):
            val, _ = max_value(game.result(state, a))
            if val < v:
                v, best = val, a
        return v, best

    player = game.player(board)
    if player == 'X':
        return max_value(board)[1]
    else:
        return min_value(board)[1]


def alphabeta(game, board):
    def max_value(state, alpha, beta):
        if game.terminal(state):
            return game.utility(state), None
        v = -inf
        best = None
        for a in sorted(game.actions(state)):
            val, _ = min_value(game.result(state, a), alpha, beta)
            if val > v:
                v, best = val, a
            if v >= beta:
                return v, best
            alpha = max(alpha, v)
        return v, best

    def min_value(state, alpha, beta):
        if game.terminal(state):
            return game.utility(state), None
        v = +inf
        best = None
        for a in sorted(game.actions(state)):
            val, _ = max_value(game.result(state, a), alpha, beta)
            if val < v:
                v, best = val, a
            if v <= alpha:
                return v, best
            beta = min(beta, v)
        return v, best

    p = game.player(board)
    if p == 'X':
        return max_value(board, -inf, +inf)[1]
    else:
        return min_value(board, -inf, +inf)[1]


def depth_limited_search(game, board, depth):
    player = game.player(board)

    def max_value(state, depth, alpha, beta):
        if game.terminal(state):
            return game.utility(state), None
        if depth == 0:
            return evaluate(game, state), None
        v = -inf
        best = None
        for a in sorted(game.actions(state)):
            val, _ = min_value(game.result(state, a), depth - 1, alpha, beta)
            if val > v:
                v, best = val, a
            if v >= beta:
                return v, best
            alpha = max(alpha, v)
        return v, best

    def min_value(state, depth, alpha, beta):
        if game.terminal(state):
            return game.utility(state), None
        if depth == 0:
            return evaluate(game, state), None
        v = +inf
        best = None
        for a in sorted(game.actions(state)):
            val, _ = max_value(game.result(state, a), depth - 1, alpha, beta)
            if val < v:
                v, best = val, a
            if v <= alpha:
                return v, best
            beta = min(beta, v)
        return v, best

    if player == 'X':
        return max_value(board, depth, -inf, +inf)[1]
    else:
        return min_value(board, depth, -inf, +inf)[1]
