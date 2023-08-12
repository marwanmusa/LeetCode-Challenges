from typing import List

class Solution:
    """
    Task:
    A peak element is an element that is strictly greater than its neighbors.

    Given a 0-indexed integer array nums, find a peak element, and return its index.
    If the array contains multiple peaks, return the index to any of the peaks.

    You may imagine that nums[-1] = nums[n] = -∞. In other words,
    an element is always considered to be strictly greater than a neighbor that is outside the array.

    You must write an algorithm that runs in O(log n) time.
    """
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 1, len(nums)-2
        n = len(nums)
        if len(nums) == 1 : return 0
        if nums[0] > nums[1]: return 0
        if nums[n-1] > nums[n-2]: return n - 1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid-1]:
                r = mid - 1
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
        return -1
    
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        # handle condition 3
        while left < right-1:
            mid = (left+right)/2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
                
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
                
        #handle condition 1 and 2
        return left if nums[left] >= nums[right] else right