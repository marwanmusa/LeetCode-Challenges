from functools import reduce

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        return reduce(lambda a, b: abs(a-b), sorted(stones, reverse=True))