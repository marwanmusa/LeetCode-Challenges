from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        cs1 = Counter(s1.split())
        cs2 = Counter(s2.split())
        ans = []
        for k in cs1:
            if cs1[k] == 1 and not cs2.get(k):
                ans.append(k)
        for k in cs2:
            if cs2[k] == 1 and not cs1.get(k):
                ans.append(k)
        return ans