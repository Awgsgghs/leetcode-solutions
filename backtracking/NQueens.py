class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def issafe(i, j):
            for row in range(n):
                if board[row][j] == 'Q':
                    return False
            for k in range(n):
                if i - k >= 0 and j - k >= 0 and board[i - k][j - k] == 'Q':
                    return False
                if i + k < n and j + k < n and board[i + k][j + k] == 'Q':
                    return False
                if i - k >= 0 and j + k < n and board[i - k][j + k] == 'Q':
                    return False
                if i + k < n and j - k >= 0 and board[i + k][j - k] == 'Q':
                    return False
            return True

        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(row, board):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for j in range(n):
                if issafe(row, j):
                    board[row][j] = 'Q'
                    backtrack(row + 1, board)
                    board[row][j] = '.'

        backtrack(0, board)
        return res
