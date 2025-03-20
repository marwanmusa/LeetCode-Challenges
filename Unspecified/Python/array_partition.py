from typing import List

class Solution:
    """
    Task:
    Given an integer array nums of 2n integers,
    group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
    such that the sum of min(ai, bi) for all i is maximized.
    Return the maximized sum.
    """
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res


    # Method 2
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])