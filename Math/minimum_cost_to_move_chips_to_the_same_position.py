from collections import Counter

class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        position = Counter(position)
        even, odd = 0, 0
        for k,v in (position.items()):
            if k & 1: odd += v
            else: even += v
        return min(even, odd)