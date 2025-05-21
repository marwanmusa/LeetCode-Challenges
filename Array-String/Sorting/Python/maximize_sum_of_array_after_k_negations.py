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


    # shorter
    def largestSumAfterKNegations(self, A: list[int], K: int) -> int:
        A.sort()
        i = 0
        while i < len(A) and i < K and A[i] < 0:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i) % 2 * min(A) * 2
