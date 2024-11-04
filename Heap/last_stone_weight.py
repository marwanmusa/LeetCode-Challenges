import bisect

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = sorted(stones)
        while len(stones) > 2:
            a, b = stones.pop(), stones.pop()
            stones.insert(bisect.bisect(stones, abs(a-b)), abs(a-b))
        return abs(stones[0] - stones[1])