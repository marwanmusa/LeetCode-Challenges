class Solution:
    """
    Task:
    Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray).
    The subsequence must be strictly increasing.

    A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is
    [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
    """
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        ans = 1
        mem = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                mem += 1
            else:
                mem = 1
            ans = max(mem, ans)
        return ans
    

    # dynamic programming
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1]+1
        return max(dp)