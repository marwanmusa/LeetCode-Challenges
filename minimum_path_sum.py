from typing import List

class Solution:
    """
    Task:
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
    which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.
    """
    # Method 1
    def minPathSum(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r and c:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
                elif not r and c:
                    grid[r][c] += grid[r][c-1]
                elif not c and r:
                    grid[r][c] += grid[r-1][c]
        return grid[-1][-1]


    # Method 2
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = [[float("inf")] * (COLS + 1) for r in range(ROWS + 1)]
        res[ROWS - 1][COLS] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        return res[0][0]