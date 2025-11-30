class TicTacToe:
    def __init__(self, m=3, k=3):
        self.m = m
        self.k = k
        self.initial = [['.' for _ in range(m)] for _ in range(m)]

    def player(self, board):
        flat = sum(board, [])
        x = flat.count('X')
        o = flat.count('O')
        return 'X' if x == o else 'O'

    def actions(self, board):
        return [(r, c)
                for r in range(self.m)
                for c in range(self.m)
                if board[r][c] == '.']

    def result(self, board, action):
        r, c = action
        p = self.player(board)
        new = [row[:] for row in board]
        new[r][c] = p
        return new

    def winner(self, board):
        lines = []

        # Rows
        for r in range(self.m):
            lines.append(board[r])

        # Columns
        for c in range(self.m):
            lines.append([board[r][c] for r in range(self.m)])

        # Diagonals
        for r in range(self.m):
            for c in range(self.m):
                # diag down-right
                dr = []
                rr, cc = r, c
                while rr < self.m and cc < self.m:
                    dr.append(board[rr][cc])
                    rr += 1
                    cc += 1
                lines.append(dr)

                # diag down-left
                dl = []
                rr, cc = r, c
                while rr < self.m and cc >= 0:
                    dl.append(board[rr][cc])
                    rr += 1
                    cc -= 1
                lines.append(dl)

        # check each line
        for line in lines:
            if len(line) < self.k:
                continue
            for i in range(len(line) - self.k + 1):
                window = line[i:i + self.k]
                if all(x == 'X' for x in window):
                    return 'X'
                if all(x == 'O' for x in window):
                    return 'O'

        return None

    def terminal(self, board):
        if self.winner(board) is not None:
            return True
        if all(cell != '.' for row in board for cell in row):
            return True
        return False

    def utility(self, board):
        w = self.winner(board)
        if w == 'X':
            return +1
        if w == 'O':
            return -1
        return 0
