from typing import List
import math
class Solution:
    """
    Task:
    Given an array nums of integers, return how many of them contain an even number of digits.
    """
    # Method 1
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            digits = 0
            while num > 0:
                num //= 10
                digits += 1
            if digits % 2 == 0:
                res += 1
        return res

    # Method 2
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if (1 + int(math.log10(num))) % 2 == 0:
                res += 1
        return res