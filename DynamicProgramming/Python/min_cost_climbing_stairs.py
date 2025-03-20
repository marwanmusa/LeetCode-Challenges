class Solution:
    # top-down dp - Time Limit Exceed
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * n
        def minCost(cost, n):
            if n < 0: return 0
            if 0 <= n <= 1: return cost[n]
            if dp[n]: return dp[n]
            dp[n] = cost[n] + min(minCost(cost, n-1), minCost(cost, n-2))
            return dp[n]
        return min(minCost(cost, n-1), minCost(cost, n-2))

    # bottom up dp
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])

    # reducing space complexity
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp1, dp2 = cost[0], cost[1]
        for i in range(2, n):
            dp1, dp2 = dp2, cost[i] + min(dp1, dp2)
        return min(dp1, dp2)