class Solution:
    """
    Task:
    We can scramble a string s to get a string t using the following algorithm:
    If the length of the string is 1, stop.
    If the length of the string is > 1, do the following:
        - Split the string into two non-empty substrings at a random index, i.e., if the string is s,
          divide it to x and y where s = x + y.
        - Randomly decide to swap the two substrings or to keep them in the same order. i.e.,
          after this step, s may become s = x + y or s = y + x.
        - Apply step 1 recursively on each of the two substrings x and y.
    Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1,
    otherwise, return false.
    """
    def isScramble(self, s1: str, s2: str) -> bool:
        return self.Memoization(s1, s2)

    def Memoization(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        cache = dict()

        def dfs(s1: str, s2: str) -> bool:
            if s1 == s2:
                return True
            key = (s1, s2) if s1 < s2 else (s2, s1)
            if key in cache:
                return cache[key]
            # Notice: reversed returns iterator, sorted returns list
            if sorted(s1) != sorted(s2):  # !!! important
                cache[key] = False
                return False
            rs2 = s2[::-1]
            for k in range(1, len(s1)):
                if dfs(s1[:k], s2[:k]) and dfs(s1[k:], s2[k:]):
                    cache[key] = True
                    return True
                if dfs(s1[:k], rs2[:k]) and dfs(s1[k:], rs2[k:]):
                    cache[key] = True
                    return True
            cache[key] = False
            return False

        return dfs(s1, s2)