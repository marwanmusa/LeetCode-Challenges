from typing import List

class Solution:
    """
    Task:
    Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

    Return any array that satisfies this condition.
    """
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        writeIdx = 0
        for readIdx in range(len(nums)):
            if nums[readIdx] % 2 == 0:
                nums[readIdx], nums[writeIdx] = nums[writeIdx], nums[readIdx]
                writeIdx += 1
        return nums