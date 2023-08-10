from typing import List

class Solution:
    """
    Task;
    Given an array of integers nums sorted in non-decreasing order,
    find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        ans = [-1, -1]

        if len(nums) == 0: return ans

        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if nums[l] != target:
            return [-1, -1]

        ans[0] = l
        r = n - 1
        while l < r:
            mid = l + (r-l+1) //2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        ans[1] = l
        return ans