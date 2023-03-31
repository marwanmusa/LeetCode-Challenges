from typing import List

class Solution:
    """
    Topic: Dynamic Programming
    Task:
    Given a rectangular pizza represented as a rows x cols matrix containing the following characters:
    'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts.

    For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary
    and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person.
    If you cut the pizza horizontally, give the upper part of the pizza to a person.
    Give the last piece of pizza to the last person.

    Return the number of ways of cutting the pizza such that each piece contains at least one apple.
    Since the answer can be a huge number, return this modulo 10^9 + 7.
    """
    # Solution 1
    def ways(self, pizza: List[str], K: int) -> int:
        m, n, MOD = len(pizza), len(pizza[0]), 10 ** 9 + 7
        preSum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                preSum[r][c] = preSum[r][c + 1] + preSum[r + 1][c] - preSum[r + 1][c + 1] + (pizza[r][c] == 'A')

        @lru_cache(None)
        def dp(k, r, c):
            if preSum[r][c] == 0: return 0
            if k == 0: return 1
            ans = 0

            for nr in range(r + 1, m):
                if preSum[r][c] - preSum[nr][c] > 0:
                    ans = (ans + dp(k - 1, nr, c)) % MOD
            for nc in range(c + 1, n):
                if preSum[r][c] - preSum[r][nc] > 0:
                    ans = (ans + dp(k - 1, r, nc)) % MOD
            return ans
        return dp(K - 1, 0, 0)


    # Solution 2
    def ways(self, pizza: List[str], k: int) -> int:
        """
        "Number of ways" indicates DP. I'll go top-down.
        """
        # Store the number of apples contained from each (row,col) pair to bottom right
        num_apples = [[0]*(len(pizza[0]) + 1) for _ in range(len(pizza) + 1)]
        for r in range(len(pizza) - 1, -1, -1):
            for c in range(len(pizza[0]) - 1, -1, -1):
                # Add the current apple + left + right - intersection
                curr_apple = 1 if pizza[r][c] == "A" else 0
                num_apples[r][c] = curr_apple + num_apples[r][c + 1] + num_apples[r + 1][c] \
                    - num_apples[r + 1][c + 1]

        @cache
        def num_ways(i: int, j: int, cuts_remaining: int) -> int:
            # i is the first row remaining
            # j is the first column remaining
            # We can either cut vertically or horizontally
            if cuts_remaining == 0:
                # Make sure that there's at least one apple remaining
                return num_apples[i][j] >= 1
            apples_remaining = num_apples[i][j]
            if apples_remaining <= cuts_remaining:
                return 0

            # Try cutting each way
            ways = 0
            for x in range(i + 1, len(pizza)):
                # Make sure we got at least one apple
                if num_apples[x][j] < apples_remaining:
                    ways += num_ways(x, j, cuts_remaining - 1)
            for y in range(j + 1, len(pizza[0])):
                if num_apples[i][y] < apples_remaining:
                    ways += num_ways(i, y, cuts_remaining - 1)
            return ways
        return num_ways(0, 0, k - 1) % (10**9 + 7)