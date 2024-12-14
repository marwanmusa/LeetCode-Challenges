class Solution:

    def helper(self, i, j):
        [a, b], [c, d] = i, j
        shortDistanceXY = min(abs(a-c), abs(b-d))
        longDistannceXY = max(abs(a-c), abs(b-d))
        return shortDistanceXY + (longDistannceXY - shortDistanceXY)

    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        ans = 0
        if n == 1: return 0
        for i in range(n - 1):
            ans += self.helper(points[i], points[i+1])
        return ans
