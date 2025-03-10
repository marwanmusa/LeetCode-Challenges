class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        le = len(grid)
        top, front, rear = le * le, 0, 0
        for i in range(le):
            maxrear, maxfront = 0, 0
            for j in range(le):
                curRear, curFront = grid[j][i], grid[i][j]
                if (curRear > maxrear): maxrear = curRear
                if (curFront > maxfront): maxfront = curFront
                if (curFront == 0): top -= 1
            rear += maxrear
            front += maxfront
        return top + front + rear