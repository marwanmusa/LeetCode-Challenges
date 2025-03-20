from functools import lru_cache
from typing import List

class Solution:
    """
    You are given an integer array nums and an integer target.

    You want to build an expression out of nums by adding one of the symbols '+'
    and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
    and concatenate them to build the expression "+2-1".

    Return the number of different expressions that you can build, which evaluates to target.
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(i, t):
            return int(t == target)\
                   if i == len(nums)\
                   else dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])

        return dfs(0, 0)
