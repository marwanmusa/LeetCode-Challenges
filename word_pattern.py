class Solution:
    """
    Task:
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
    """
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s): return False
        return len(set(zip(pattern, s))) == len(set(s)) == len(set(pattern))