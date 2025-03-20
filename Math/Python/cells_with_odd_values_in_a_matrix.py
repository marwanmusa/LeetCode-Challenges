class Solution:
    def rfill(self, matrix: list, r: int, n):
        for i in range(n):
            matrix[r][i] += 1

    def cfill(self, matrix: list, c: int, m):
        for i in range(m):
            matrix[i][c] += 1

    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]
        ans = 0
        for r, c in indices:
            self.rfill(matrix, r, n)
            self.cfill(matrix, c, m)

        for i in range(len(matrix)):
            ans += sum(n & 1 for n in matrix[i])

        return ans


    # simpler one
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        # rows[i] and cols[i] :=
        #   1. True (flipped even times)
        #   2. False (flipped odd times)
        rows = [False] * m
        cols = [False] * n

        for r, c in indices:
            rows[r] ^= True
            cols[c] ^= True

        oddRowsCount = rows.count(True)
        oddColsCount = cols.count(True)
        evenRowsCount = m - oddRowsCount
        evenColsCount = n - oddColsCount
        return oddRowsCount * evenColsCount + oddColsCount * evenRowsCount
