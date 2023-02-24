class Solution:
    """
    Task:
    Given a string s, find the first non-repeating character in it and return its index.
    If it does not exist, return -1.
    """
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.rindex(i) == s.index(i):
                return s.index(i)
        return -1