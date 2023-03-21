from typing import List
class Solution:
    """
    Task:
    Given an integer array nums, return the number of subarrays filled with 0.

    A subarray is a contiguous non-empty sequence of elements within an array.
    """
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = prev = 0
        for x in nums:
            if x == 0: prev += 1
            else: prev = 0
            res += prev
        return res