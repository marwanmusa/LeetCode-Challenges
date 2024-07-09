class Solution:
    """
    Task:
    Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

    The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
    """
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n, pos = len(S), -float('inf')
        res = [n] * n
        for i in range(n) + range(n)[::-1]:
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res