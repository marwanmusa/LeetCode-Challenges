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
        