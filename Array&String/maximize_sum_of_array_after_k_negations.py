class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        negs = sorted([x for x in nums if x < 0])
        pos = sorted([x for x in nums if x >= 0])
        n = len(negs)
        for i in range(min(k, n)):
            negs[i] = -negs[i]
        k -= min(k, n)
        negs = sorted(negs + pos)
        if k:
            negs[0] = -negs[0] if k % 2 else pos[0]
            return sum(negs)
        return sum(negs)