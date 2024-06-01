import collections
class Solution:
    # variation 1
    def judgeCircle(self, moves: str) -> bool:
        d = collections.defaultdict(int)
        for w in moves:
            d[w] += 1
        return True if d['U'] - d['D'] == 0 and d['L'] - d['R'] == 0 else False
    
    # variation 2
    def judgeCircle(self, moves: str) -> bool:
        return not any([moves.count(a[0]) - moves.count(a[1]) for a in ["LR", "UD"]])
    
    # variation 3
    def judgeCircle(self, moves: str) -> bool:
        return all([moves.count(a[0]) == moves.count(a[1]) for a in ["LR", "UD"]])