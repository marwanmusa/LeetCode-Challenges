from typing import List
class Solution:
    """
    Task:
    Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

    Return the minimized largest sum of the split.

    A subarray is a contiguous part of the array.
    """
    # Parametric search
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r-l) // 2
            tot, cnt = 0, 1
            for num in nums:
                if tot  + num <= mid:
                    tot += num
                else:
                    tot = num
                    cnt += 1
            if cnt > k: l = mid + 1
            else: r = mid
        return r
    
    # Brute Force
    def helper(self, nums: List[int], k: int) -> int:
        if nums == []: return 0
        elif k == 1: return sum(nums)
        else:
            min_res = float('inf')
            for j in range(1, len(nums)+1):
                l, r = sum(nums[:j]), self.helper(nums[j:], k-1)
                min_res = min(min_res, max(l, r))
            return min_res
    
    def splitArray(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k)
        