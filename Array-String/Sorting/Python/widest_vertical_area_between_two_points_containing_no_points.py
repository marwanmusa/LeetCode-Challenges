class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x: x[0])
        n, res = len(points), 0
        for i in range(1, n):
            res = max(res, points[i][0] - points[i-1][0])
        return res

    # one liner
    def maxWidthOfVerticalArea2(self, points: list[list[int]]) -> int:
        return max(points[i][0] - points[i-1][0] for i in range(1, len(points)))