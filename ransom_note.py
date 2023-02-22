class Solution:
    """
    Task:
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed
    by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote
    """
    # Method 1
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn, mg = list(ransomNote), list(magazine)
        c = len(rn)
        i = 0
        while i<len(rn):
            for j in mg:
                if rn[i] == j:
                    mg.remove(j)
                    c -= 1
                    break
            i += 1
        return c == 0

    # Method 2 - MORE EFFICIENT WAY
    def canConstruct(self, r: str, m: str) -> bool:
        for i in set(r):
            if i not in m or r.count(i)>m.count(i):
                return False
        return True