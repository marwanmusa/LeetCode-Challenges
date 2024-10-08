class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        smalls = sorted([x for x in nums if x < 0])
        pos = [x for x in nums if x >= 0]
        n = len(smalls)
        for i in range(min(k, n)):
            smalls[i] = -smalls[i]
        k -= min(k, n)
        smalls = sorted(smalls + pos)
        if k and k % 2: smalls[0] = -smalls[0]
        return sum(smalls)
