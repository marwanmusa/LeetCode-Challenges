from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        cs = Counter((s1 + " " + s2).split())
        ans = []
        for k in cs:
            if cs[k] == 1:
                ans.append(k)
        return ans