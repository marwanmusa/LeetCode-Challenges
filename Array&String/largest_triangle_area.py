import itertools

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        return max(0.5 * abs(i[0]*j[1] + j[0]*k[1] + k[0]*i[1] - i[0]*k[1] - k[0]*j[1] - j[0]*i[1])
                   for i, j, k in itertools.combinations(points, 3))