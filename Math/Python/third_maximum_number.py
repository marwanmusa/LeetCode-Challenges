from typing import List
from numpy import inf

class Solution:
    """
    Task:
    Given an integer array nums, return the third distinct maximum number in this array.
    If the third maximum does not exist, return the maximum number.
    """
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = -inf
        sec_max  = -inf
        third_max = -inf
        for n in nums:
            if max_nums == n or sec_max == n or third_max == n:
                continue
            if n >= max_nums:
                third_max = sec_max
                sec_max = max_nums
                max_nums = n
            elif sec_max <= n:
                third_max = sec_max
                sec_max = n
            elif third_max <= n:
                third_max = n
        if third_max == -inf:
            return max_nums
        return third_max