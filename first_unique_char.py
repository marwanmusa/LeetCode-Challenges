from collections import defaultdict

class Solution:
    """
    Task:
    Given a string s, find the first non-repeating character in it and return its index.
    If it does not exist, return -1.
    """
    # Method 0
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.rindex(i) == s.index(i):
                return s.index(i)
        return -1


    # Method 1
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for word in s:
            d[word] += 1
        first = ""
        for key in d:
            if d[key] == 1:
                first += key
                break
        for i, word in enumerate(s):
            if word == first:
                return i
        return -1


    # Method 2
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        for i in range(len(s)):
            if s[i] in seen:
                continue
            try:
                s.index(s[i], s.index(s[i], 0) + 1)
            except:
                return i
            seen.add(s[i])
        return -1