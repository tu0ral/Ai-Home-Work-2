def evaluate(game, board):
    """
    Simple threat-based heuristic:
    +100 for each (k-1)-in-a-row for X
    -100 for each (k-1)-in-a-row for O
    +10 for each (k-2)-in-a-row
    """

    m, k = game.m, game.k
    score = 0

    lines = []

    # rows
    for r in range(m):
        lines.append(board[r])

    # cols
    for c in range(m):
        lines.append([board[r][c] for r in range(m)])

    # diagonals
    for r in range(m):
        for c in range(m):
            # diag right
            dr = []
            rr, cc = r, c
            while rr < m and cc < m:
                dr.append(board[rr][cc])
                rr += 1
                cc += 1
            lines.append(dr)

            # diag left
            dl = []
            rr, cc = r, c
            while rr < m and cc >= 0:
                dl.append(board[rr][cc])
                rr += 1
                cc -= 1
            lines.append(dl)

    for line in lines:
        for i in range(len(line) - k + 1):
            window = line[i:i+k]
            if window.count('X') == k - 1 and window.count('.') == 1:
                score += 100
            if window.count('O') == k - 1 and window.count('.') == 1:
                score -= 100

            if window.count('X') == k - 2 and window.count('.') == 2:
                score += 10
            if window.count('O') == k - 2 and window.count('.') == 2:
                score -= 10

    return score
