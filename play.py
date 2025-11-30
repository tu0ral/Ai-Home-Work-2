from engine import TicTacToe
from search import alphabeta, depth_limited_search


# CONFIG
HUMAN_PLAYER = 'X'   # 'X' or 'O'
AI_DEPTH = 4         # for m > 3 boards

def print_board(board):
    print("\nBoard:")
    for r, row in enumerate(board):
        print(f"{r} | " + " ".join(row))
    print("    " + " ".join(str(c) for c in range(len(board))))


def get_human_move(game, board):
    actions = set(game.actions(board))
    while True:
        try:
            raw = input("Enter your move as 'row col': ")
            parts = raw.strip().split()
            if len(parts) != 2:
                print("Please enter exactly two integers: row col")
                continue
            r, c = int(parts[0]), int(parts[1])
            move = (r, c)
            if move not in actions:
                print("Illegal move, choose an empty cell on the board.")
                continue
            return move
        except ValueError:
            print("Invalid input, please enter integers like: 1 2")


def choose_ai_move(game, board):
    m, k = game.m, game.k
    # 3x3 full depth search can be okay, but we already have AB + heuristic.
    if m == 3 and k == 3:
        # full AB (no depth limit) is feasible
        from math import inf

        # simple full-depth alpha-beta using utility (no heuristic)
        from engine import TicTacToe as _T

        # but we already have alphabeta that stops at terminal
        return alphabeta(game, board)
    else:
        return depth_limited_search(game, board, depth=AI_DEPTH)


def main():
    g = TicTacToe(m=3, k=3)   # change m,k for different board sizes
    board = g.initial

    print("=== Generalized Tic-Tac-Toe ===")
    print(f"Board size: {g.m}x{g.m}, k={g.k}")
    print(f"You are: {HUMAN_PLAYER}")
    print("Coordinates start from 0 (row, col).")

    while not g.terminal(board):
        print_board(board)
        current = g.player(board)

        if current == HUMAN_PLAYER:
            print("Your turn.")
            move = get_human_move(g, board)
        else:
            print("AI is thinking...")
            move = choose_ai_move(g, board)
            print(f"AI plays: {move}")

        board = g.result(board, move)

    print_board(board)
    print("\n=== Game Over ===")
    w = g.winner(board)
    if w is None:
        print("Result: Draw.")
    elif w == HUMAN_PLAYER:
        print("You win! 🎉")
    else:
        print("AI wins. 🤖")

if __name__ == "__main__":
    main()
