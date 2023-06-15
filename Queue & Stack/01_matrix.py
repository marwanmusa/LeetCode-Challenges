from collection import deque
from typing import List

class Solution:
    """
    Task:
    Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

    The distance between two adjacent cells is 1.
    """
    # bfs 1
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        h, w = len(mat), len(mat[0])
        q = []

        for i in range(h):
            for j in range(w):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = '#'

        for row, col in q:
            for dx, dy in (1,0), (-1,0), (0,1), (0,-1):
                nr = row + dx
                nc = col + dy

                if 0 <= nr < h and 0 <= nc < w and mat[nr][nc] == '#':
                    mat[nr][nc] = mat[row][col] + 1
                    q.append((nr, nc))

        return mat


    # bfs 2
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1 # marked as not processed yet

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))

        return mat