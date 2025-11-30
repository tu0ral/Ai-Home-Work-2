# test_tictactoe.py

import itertools

from engine import TicTacToe
from search import minimax, alphabeta, depth_limited_search
from heuristic import evaluate


def test_initial_state():
    g = TicTacToe(m=3, k=3)
    b = g.initial
    # All cells empty
    assert all(cell == '.' for row in b for cell in row)
    # Current player must be X
    assert g.player(b) == 'X'
    # 9 legal moves
    assert len(g.actions(b)) == 9


def test_player_turns():
    g = TicTacToe(m=3, k=3)
    b = g.initial
    # X moves
    b1 = g.result(b, (0, 0))
    assert g.player(b1) == 'O'
    # O moves
    b2 = g.result(b1, (1, 1))
    assert g.player(b2) == 'X'


def test_winner_row():
    g = TicTacToe(m=3, k=3)
    b = [
        ['X', 'X', 'X'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    assert g.winner(b) == 'X'
    assert g.terminal(b) is True
    assert g.utility(b) == 1


def test_winner_col():
    g = TicTacToe(m=3, k=3)
    b = [
        ['O', '.', '.'],
        ['O', '.', '.'],
        ['O', '.', '.']
    ]
    assert g.winner(b) == 'O'
    assert g.terminal(b) is True
    assert g.utility(b) == -1


def test_winner_diag_main():
    g = TicTacToe(m=3, k=3)
    b = [
        ['X', '.', '.'],
        ['.', 'X', '.'],
        ['.', '.', 'X']
    ]
    assert g.winner(b) == 'X'
    assert g.terminal(b) is True
    assert g.utility(b) == 1


def test_winner_diag_anti():
    g = TicTacToe(m=3, k=3)
    b = [
        ['.', '.', 'O'],
        ['.', 'O', '.'],
        ['O', '.', '.']
    ]
    assert g.winner(b) == 'O'
    assert g.terminal(b) is True
    assert g.utility(b) == -1


def test_draw_terminal():
    g = TicTacToe(m=3, k=3)
    b = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    assert g.winner(b) is None
    assert g.terminal(b) is True
    assert g.utility(b) == 0


def test_minimax_vs_alphabeta_empty_3x3():
    g = TicTacToe(m=3, k=3)
    b = g.initial
    move_mm = minimax(g, b)
    move_ab = alphabeta(g, b)
    assert move_mm == move_ab


def test_minimax_vs_alphabeta_random_3x3():
    # Some random mid-game positions
    g = TicTacToe(m=3, k=3)
    # Example board:
    # X O X
    # . O .
    # . . .
    b = [
        ['X', 'O', 'X'],
        ['.', 'O', '.'],
        ['.', '.', '.']
    ]
    move_mm = minimax(g, b)
    move_ab = alphabeta(g, b)
    assert move_mm == move_ab


def test_heuristic_symmetry_empty():
    g = TicTacToe(m=4, k=3)
    b = g.initial
    assert evaluate(g, b) == 0


def test_heuristic_detects_threats():
    g = TicTacToe(m=4, k=3)
    # X has XX. in a row -> should be positive
    b1 = [
        ['X', 'X', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
    ]
    # O has OO. in a row -> should be negative
    b2 = [
        ['O', 'O', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
    ]
    v1 = evaluate(g, b1)
    v2 = evaluate(g, b2)
    assert v1 > 0
    assert v2 < 0


def test_depth_limited_takes_immediate_win():
    g = TicTacToe(m=3, k=3)
    # X to move and can win immediately
    b = [
        ['X', 'X', '.'],
        ['O', 'O', '.'],
        ['.', '.', '.']
    ]
    # X is player (2 X, 2 O -> X's turn)
    assert g.player(b) == 'X'
    move = depth_limited_search(g, b, depth=1)
    # Winning move is (0, 2)
    assert move == (0, 2)


def test_depth_limited_blocks_immediate_threat():
    g = TicTacToe(m=3, k=3)
    # O threatens to win, X must block
    # Board:
    # O O .
    # X X .
    # . . .
    b = [
        ['O', 'O', '.'],
        ['X', 'X', '.'],
        ['.', '.', '.']
    ]
    # Count: X=2, O=2 -> X to move
    assert g.player(b) == 'X'
    move = depth_limited_search(g, b, depth=2)
    # Best is to block O at (0, 2)
    assert move == (0, 2)
