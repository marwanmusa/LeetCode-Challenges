from collections import defaultdict
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        d = defaultdict(int)
        morethan1 = False
        mismatch = 0
        for i in range(len(s)):
            d[s[i]] += 1
            morethan1 = d[s[i]] > 1
            if s[i] != goal[i]: 
                mismatch += 1
                if mismatch > 2: return False
        if not mismatch and not morethan1:
            return False
        return True