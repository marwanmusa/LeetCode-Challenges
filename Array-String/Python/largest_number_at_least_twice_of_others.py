from typing import List

class Solution:
    """
    Task:
    You are given an integer array nums where the largest integer is unique.

    Determine whether the largest element in the array is at least twice as much as every other number in the array.
    If it is, return the index of the largest element, or return -1 otherwise.
    """
    def dominantIndex(self, nums: List[int]) -> int:
        largestNum = 0
        maxIndex = 0
        for i in range(len(nums)):
            if nums[i] > largestNum:
                maxIndex = i
                largestNum = nums[i]
        for num in nums:
            if num != largestNum and ((2*num) > largestNum):
                return -1
        return maxIndex


    # Using python built-in max and list.index
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        for a in nums:
            if a != mx and a * 2 > mx:
                return -1
        return nums.index(mx)