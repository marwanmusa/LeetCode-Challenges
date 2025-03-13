class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if not trust: return n if n == 1 else -1

        fr, to = set(), {}

        for a, b in trust:
            fr.add(a)

            if a in to:
                to.pop(a)

            if b not in fr:
                to[b] = to.get(b, 0) + 1

        if (len(to) > 1 or not to or len(fr) >= n):
            return -1
        else:
            judge = next(iter(to))
            if to[judge] == n-1: return judge
            else: return -1
