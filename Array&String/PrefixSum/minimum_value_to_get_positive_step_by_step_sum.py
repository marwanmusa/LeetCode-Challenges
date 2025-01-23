class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        minval, sumv = 0, 0
        for x in nums:
            sumv += x
            minval = min(minval, sumv)
        return 1 - minval