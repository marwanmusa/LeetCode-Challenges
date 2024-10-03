from collections import Counter
from functools import reduce
from operator import and_

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        temp = Counter(words[0])
        for i in range(1, len(words)):
            cur = Counter(words[i])
            calc = {w: min(cur[w], temp[w]) for w in (cur.keys() & temp.keys())}
            temp = calc
        ans = []
        for k in temp:
            ans.extend([k] * temp[k])
        return ans

    # shorter
    def commonChars(self, A: list[str]) -> list[str]:
        res = Counter(A[0])
        for a in A:
            res &= Counter(a)
        return list(res.elements())

    # one-liner
    def commonChars(self, A: list[str]) -> list[str]:
        return reduce(and_, map(Counter, A)).elements()