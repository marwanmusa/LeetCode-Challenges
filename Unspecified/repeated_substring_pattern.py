class Solution:
    """
    Task:
    Given a string s, check if it can be constructed by taking a substring of it
    and appending multiple copies of the substring together.
    """
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_fold = "".join((s[1:], s[:-1]))
        return s in s_fold
    
    # optimizing prev approach
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s[1:]+s[:-1]).find(s) >= 0
    
    # brute force approach
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, len(s)//2 + 1):
            if n % i == 0:
                sub = s[:i]
                if sub[:i] * (n // i) == s:
                    return True
        return False