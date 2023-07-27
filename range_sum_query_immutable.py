"""
Task:
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
  (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""
from typing import List


# Solution 1 (slow)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, l: int, r: int) -> int:
        ans = 0
        for i in range(l, r + 1):
            ans += self.nums[i]
        return ans


# Solution 2 (faster)
class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = nums
        for i in range(len(nums)-1):
            self.preSum[i+1] += self.preSum[i]

    def sumRange(self, l: int, r: int) -> int:
        if l == 0: return self.preSum[r]
        return self.preSum[r] - self.preSum[l-1]