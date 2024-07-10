class Solution:
    """
    Task:
    Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

    The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
    """
    def shortestToChar(self, s: str, c: str) -> list[int]:
        loc = []
        ans = []
        for i, e in enumerate(s):
            if e == c: loc.append(i)
        if len(loc) == 1:
            ans += range(loc[0], -1 , -1)
            ans += range()
        return []

    def create_pascal(n):
        dp = [0] * n
        if n & 1:
            for i in range(1, n):
                if i <= n//2:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-1] - 1
        else:
            dp[:n//2] = range(n//2)
            dp[n//2:] = range(n//2-1, -1, -1)
        return dp