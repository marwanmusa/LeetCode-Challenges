class Solution:
    """
    Task:
    Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

    The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
    """
    def shortestToChar(self, s: str, c: str) -> list[int]:
        last = -1
        op = False
        ans = []
        for i, e in enumerate(s):
            if e == c: 
                if last < 0:
                    ans += range(i, -1, -1)
                else:
                    ans += self.create_pascal(i - last + 1)[1:]
                last = i
        if i == len(s)-1 and i != last:
            ans += range(1, i-last+1)
        return ans
            

    def create_pascal(self, n):
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