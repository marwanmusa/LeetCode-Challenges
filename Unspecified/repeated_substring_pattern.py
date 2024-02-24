class Solution:
    """
    Task:
    Given a string s, check if it can be constructed by taking a substring of it
    and appending multiple copies of the substring together.
    """
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_fold = "".join((s[1:], s[:-1]))
        return s in s_fold