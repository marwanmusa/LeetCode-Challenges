from math import ceil
from typing import List

class Solution:
    """
    Task:
    You are given a 0-indexed array nums comprising of n non-negative integers.

    In one operation, you must:
        - Choose an integer i such that 1 <= i < n and nums[i] > 0.
        - Decrease nums[i] by 1.
        - Increase nums[i - 1] by 1.
    Return the minimum possible value of the maximum integer of nums after performing any number of operations.
    """
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # I. The max possible value between two adjacent elements
        #    is their average (rounded up).
        #
        # II. The max between three or more elements
        #    is the average of largest and smallest.
        #
        # III. Moving only in one direction (right to left)
        #    Thus, if the largest is first it cannot be changed
        #        and elements after largest doesn't count
        #
        # Thus, return the first if largest or avg between smallest and largest
        max_num = sum_num = nums[0]
        for i in range(1, len(nums)):
            sum_num += nums[i]
            avg = ceil(sum_num / (i + 1))
            if max_num < avg:
                max_num = avg

        return max_num