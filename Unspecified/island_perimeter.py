class Solution:
    """
    You are given row x col grid representing a map where grid[i][j] = 1 represents land
    and grid[i][j] = 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water
    and there is exactly one island (i.e., one or more connected land cells).

    The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
    One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
    Determine the perimeter of the island.
    """
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m, n, perimeter = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                perimeter += 4*grid[i][j]
                if i > 0: perimeter -= grid[i][j]*grid[i-1][j]
                if i < m-1: perimeter -= grid[i][j]*grid[i+1][j]
                if j > 0: perimeter -= grid[i][j]*grid[i][j-1]
                if j < n-1: perimeter -= grid[i][j]*grid[i][j+1]
        return perimeter
    

if __name__ == '__main__':
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(Solution().islandPerimeter(grid))