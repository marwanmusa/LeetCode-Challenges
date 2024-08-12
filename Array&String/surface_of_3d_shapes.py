class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        ans, m, n =0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]: ans += 2 + 4 * grid[i][j]
                if i+1 < m: ans -= min(grid[i][j], grid[i+1][j])
                if j+1 < n: ans -= min(grid[i][j], grid[i][j+1])
                if i: ans -= min(grid[i][j], grid[i-1][j])
                if j: ans -= min(grid[i][j], grid[i][j-1])
        return ans
        