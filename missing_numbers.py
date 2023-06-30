from typing import List

class Solution:
    """
    Task:
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
    """
    # sum
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1))-sum(nums)

    # or
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Get sum of complete series(Gaussian formula)
        # and find the difference between sum of given series
        return ((n * (n+1)) // 2 ) - sum(nums) 