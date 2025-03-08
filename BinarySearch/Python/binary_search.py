class Solution:
    """
    Task:
    Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity
    """
    # Iterative approach
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        return -1

    # Recursive approach
    def search(self, nums: list[int], x: int) -> int:
        def binary_search(nums: list[int], lo, hi):
            if hi >= lo:
                mid = lo + (hi - lo)//2
                if x == nums[mid]:
                    return mid
                elif x > nums[mid]:
                    return binary_search(nums, mid+1, hi)
                else:
                    return binary_search(nums, lo, mid-1)
            return -1
        return binary_search(nums, 0, len(nums)-1)