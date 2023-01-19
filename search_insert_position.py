class Solution:
    """
    Task:
    Given a sorted array of distinct integers and a target value,
    return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.
    """
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target < min(nums):
            return 0
        elif target > max(nums):
            return nums.index(max(nums)) + 1
        elif target in nums:
            return nums.index(target)
        else:
            i = 0
            while i < len(nums):
                if nums[i] < target < nums[i + 1]:
                    return i+1
                i += 1