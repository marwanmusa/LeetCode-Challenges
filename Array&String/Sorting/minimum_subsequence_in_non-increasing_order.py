class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        if len(nums) == 1: return nums
        nums.sort(reverse = True)
        res, total, l = [nums[0]], sum(nums), nums[0]
        for i in range(1, len(nums)):
            if (l > total - l) : break
            l += nums[i]
            res.append(nums[i])
        return res
