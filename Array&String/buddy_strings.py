from collections import defaultdict, Counter
class Solution:
    # not cover all test cases, 30 / 39 testcases passed
    def buddyStrings(self, s: str, goal: str) -> bool:
        m, n = Counter(s), Counter(goal)
        mk, nk = len(m.keys()), len(n.keys())
        if mk < nk or mk > nk: return False
        morethan1 = False
        for k in n:
            if not m.get(k): return False
            if m.get(k) > 1 and n.get(k) > 1:
                morethan1 = True
        if not morethan1 and s == goal: return False
        return True