from typing import List

class Solution:
    """
    Task:
    You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
    connected 4-directionally (horizontal or vertical.)
    You may assume all four edges of the grid are surrounded by water.

    The area of an island is the number of cells with a value 1 in the island.

    Return the maximum area of an island in grid. If there is no island, return 0.
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r: int, c: int) -> int:
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c)
                      + dfs(r - 1, c)
                      + dfs(r, c + 1)
                      + dfs(r, c - 1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        return area