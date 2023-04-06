from typing import List
from queue import Queue


class Solution:
    """
    Task:
    Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s
    and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

    Return the number of closed islands.
    """
    # Using DFS
    def closedIsland(self, grid: List[List[int]]) -> int:

        n = len(grid[0])
        m = len(grid)

        def dfs(board, r, c):
            if r <0 or c< 0 or r >=m or c >= n: return
            if board[r][c] != 0: return
            board[r][c] = 1
            dfs(board, r-1, c)
            dfs(board, r, c-1)
            dfs(board, r+1, c)
            dfs(board, r, c+1)


        for r in range(m):
            dfs(grid, r, 0)
            dfs(grid, r, n-1)

        for c in range(n):
            dfs(grid, 0, c)
            dfs(grid, m-1, c)

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    count += 1
                    dfs(grid, r, c)

        return count


    # Using BFS
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        def bfs(x: int, y: int) -> bool:
            q = Queue()
            q.put((x, y))
            visit[x][y] = True
            isClosed = True
            dirx, diry = [0, 1, 0, -1], [-1, 0, 1, 0]

            while not q.empty():
                x, y = q.get()
                for i in range(4):
                    r, c = x + dirx[i], y + diry[i]
                    if r < 0 or r >= m or c < 0 or c >= n:
                        isClosed = False
                    elif grid[r][c] == 0 and not visit[r][c]:
                        q.put((r, c))
                        visit[r][c] = True

            return isClosed

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visit[i][j] and bfs(i, j):
                    count += 1

        return count