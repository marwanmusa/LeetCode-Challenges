class Solution:
    """
    Task:
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character
    while preserving the order of characters. No two characters may map to the same character,
    but a character may map to itself.
    """
    # Method 1
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        res = {}
        for i in range(len(s)):
            ws, wt = s[i], t[i]
            if ws not in res:
                if wt in res.values():
                    return False
                res[ws] = wt
            elif res[ws] != wt:
                return False
        return True

    # Method 2
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i,j in zip(s,t):
            if i not in d1 and j not in d2:
                d1[i]=j
                d2[j]=i
            elif d1.get(i)!=j or d2.get(j)!=i:
                return False
        return True