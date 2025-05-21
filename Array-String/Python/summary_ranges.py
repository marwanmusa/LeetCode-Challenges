from typing import List

class Solution:
    """
    Task:
    You are given a sorted unique integer array nums.
    A range [a,b] is the set of all integers from a to b (inclusive).
    Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
    That is, each element of nums is covered by exactly one of the ranges,
    and there is no integer x such that x is in one of the ranges but not in nums.

    Each range [a,b] in the list should be output as:
        - "a->b" if a != b
        - "a" if a == b
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l,r = 0, 0
        length = len(nums)
        result = []
        while r < length:
            while r + 1 < length and nums[r+1] == nums[r]+1:
                r += 1

            if l == r:
                result.append(str(nums[l]))
            else:
                result.append(str(nums[l]) + "->" + str(nums[r]))
            r += 1
            l = r
        return result


    # Method 2
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] == nums[j - 1] + 1: j += 1
            if j == i + 1:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[j - 1]))
            i = j
        return res