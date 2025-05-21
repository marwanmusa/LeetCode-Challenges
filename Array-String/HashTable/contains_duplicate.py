from typing import List

class Solution:
    """
    Task:
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    """
    # Method 1
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


    # Method 2
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False