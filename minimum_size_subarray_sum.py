from typing import List

class Solution:
    """
    Task:
    Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
    whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
    """
    # Method 1
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None:
            return nums
        if len(nums) == 1:
            if nums[0] >= target: return 1
            else: return 0
        n = len(nums)
        ans = float('inf')
        l, s = 0, 0
        for i in range(n):
            s += nums[i]
            while s >= target:
                ans = min(ans, i + 1 - l)
                s -= nums[l]
                l += 1
        return ans if ans != float('inf') else 0


    # Method 2
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, window_sum = 0, 0
        shortest = float('inf')
        for end in range(len(nums)):
            window_sum += nums[end]
            while window_sum >= target:
                shortest = min(shortest, end - start + 1)
                window_sum -= nums[start]
                start += 1
        return shortest if shortest != float('inf') else 0