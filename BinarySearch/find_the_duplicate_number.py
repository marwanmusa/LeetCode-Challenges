from typing import List

class Solution:
    """
    Task:
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.
    """

    # Approach 1: Sort
    """
    Note: This approach modifies individual elements and does not use constant space,
    and hence does not meet the problem constraints.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
    
    # Approach 2: Set
    """
    Note: This approach does not use constant space, and hence does not meet the problem constraints.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
    
    # Approach 3: Negative Marking
    """
    Note: This approach temporarily modifies individual elements and thus does not satisfy the problem constraints.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # mark all negative numbers as visited (negative marking technique)
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]

        # restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        
        return duplicate
    
