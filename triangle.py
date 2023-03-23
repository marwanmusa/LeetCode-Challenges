from typing import List

class Solution:
    """
    Task:
    Given a triangle array, return the minimum path sum from top to bottom.

    For each step, you may move to an adjacent number of the row below.
    More formally, if you are on index i on the current row,
    you may move to either index i or index i + 1 on the next row.
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])

        return dp[0]