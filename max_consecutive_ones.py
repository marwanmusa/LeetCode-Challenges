from typing import List

class Solution:
    """
    Task:
    Given a binary array nums, return the maximum number of consecutive 1's in the array.
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                max_ones = max(max_ones, ones)
                ones = 0
        max_ones = max(max_ones, ones)
        return max_ones