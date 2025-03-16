class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        if len(nums) == 1: return nums
        nums.sort()
        res, total, r = [], sum(nums), 0
        for i in range(len(nums)-1, -1, -1):
            if (r > total - r) : break
            r += nums[i]
            res.append(nums[i])
        return res
