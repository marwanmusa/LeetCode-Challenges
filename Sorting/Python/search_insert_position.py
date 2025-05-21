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

    # Using binary search algorithm, time complexity O(Log(n))
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums) - 1
        l, r = 0, n
        if target < nums[l]:
            return 0
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l