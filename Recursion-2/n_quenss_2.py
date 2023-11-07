class Solution:
    """
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

    Given an integer n, return the number of distinct solutions to the n-queens puzzle.
    """
    # Approach 1
    def totalNQueens(self, n: int) -> int:
        diag1 = set()
        diag2 = set()
        used_cols = set()
        return self.helper(n, diag1, diag2, used_cols, 0)

    def helper(self, n, diag1, diag2, used_cols, row):
        if row == n:
            return 1

        solutions = 0

        for col in range(n):
            if row + col in diag1 or row - col in diag2 or col in used_cols:
                continue

            diag1.add(row + col)
            diag2.add(row - col)
            used_cols.add(col)

            solutions += self.helper(n, diag1, diag2, used_cols, row+1)

            diag1.remove(row + col)
            diag2.remove(row - col)
            used_cols.remove(col)
        return solutions

    # Approach 1 shorter
    def totalNQueens(self, n: int, diag1: set = set(), diag2: set = set(), used_cols: set = set(), row: int = 0) -> int:
        if row == n: return 1

        solutions = 0

        for col in range(n):
            if (row+col) in diag1 or (row-col) in diag2 or col in used_cols:
                continue

            diag1.add(row+col)
            diag2.add(row-col)
            used_cols.add(col)

            solutions += self.totalNQueens(n, diag1, diag2, used_cols, row+1)

            diag1.remove(row+col)
            diag2.remove(row-col)
            used_cols.remove(col)
        return solutions
    
    # Short backtracking
    def totalNQueens(self, n: int) -> int:
        def dfs(board, i, c1, c2, c3):
            if i == n:
                self.ans += 1
            for j in range(n):
                if c1 & 1<<j or c2 & 1<<i-j+n or c3 & 1<<i+j:
                    continue
                dfs(board + [j], i + 1, c1 ^ 1<<j, c2 ^ 1<<i-j+n, c3 ^ 1<<i+j)
        
        self.ans = 0
        dfs([], 0, 0, 0, 0)
        return self.ans