class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        return max(max(nums) - min(nums) - 2*k, 0)