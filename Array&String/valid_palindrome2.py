class Solution:
    """
    Task:
    Given a string s, return true if the s can be palindrome after deleting at most one character from it.
    """
    def validPalindrome(self, s: str) -> bool:
        def solve(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        n = len(s)
        if n <= 2: return True
        if s == s[::-1]: return True
        i, j = 0, n-1
        while i < j:
            if s[i] != s[j]:
                if solve(s, i, j-1) or solve(s, i+1, j):
                    return True
                else:
                    return False
            i += 1
            j -= 1
        return True