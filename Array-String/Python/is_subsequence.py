class Solution:
    """
    Task:
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original stringby deleting
    some (can be none) of the characters without disturbing the relative positions of the remaining characters.
    (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    """
    # Method 1
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
        return i == len(s)


    # Method 2
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        ptr = 0
        for ch in t:
            if ch == s[ptr]:
                ptr += 1
            if ptr >= len(s):
                return True
        return False