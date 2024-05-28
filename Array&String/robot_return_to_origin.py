import collections
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = collections.defaultdict(int)
        for w in moves:
            d[w] += 1
        return True if d['U'] - d['D'] == 0 and d['L'] - d['R'] == 0 else False