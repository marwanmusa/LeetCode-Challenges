class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        r, c = len(grid), len(grid[0])
        k = k % (r*c)

        grid = [x for mat in grid for x in mat]
        grid = grid[-k:] + grid[:-k]

        res = []
        for i in range(r):
            res.append(grid[i*c : (i+1)*c])
        return res