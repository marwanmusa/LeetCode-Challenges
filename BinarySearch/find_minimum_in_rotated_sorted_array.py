from typing import List

class Solution:
    """
    Task:
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
    For example, the array nums = [0,1,2,4,5,6,7] might become:
        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.

    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, return the minimum element of this array.

    You must write an algorithm that runs in O(log n) time.
    """
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        if nums[l] < nums[r]:
            return nums[l]
        else:
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l]
    
    # Method 2
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:  # The nums[mid] is the minimum number
                return nums[mid]
            if nums[mid] > nums[right]:  # search on the right side, because smaller elements are in the right side
                left = mid + 1
            else:
                right = mid - 1  # search the minimum in the left side