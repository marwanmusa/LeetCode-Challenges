class Solution:
    """
    Task:
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
    such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.
    """
    # Using pivot
    def search(self, nums: list[int], target: int) -> int:
        def binarySearch(left, right, pivot) -> int:
            while left <= right:
                print(left, right)
                mid = left + (right - left) // 2
                if nums[(mid + pivot) % len(nums)] > target:
                    right = mid - 1
                elif nums[(mid + pivot) % len(nums)] < target:
                    left = mid + 1
                else:
                    return (mid + pivot) % len(nums)
            return -1
        pivot = nums.index(min(nums)) # This code make this solution O(N) time complexity
        left, right = 0, len(nums) - 1
        index = binarySearch(left, right, pivot)
        return index

    # Adjusment, O(LogN) time complexity
    def search(self, nums: list[int], target: int) -> int:
        r = len(nums) - 1
        l = 0
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            elif nums[m] >= nums[l]:
                if (target > nums[m]) or (target < nums[m] and target < nums[l]):
                    l = m+1
                else:
                    r = m-1
            else:
                if (target < nums[m]) or (target > nums[m] and target > nums[r]):
                    r = m-1
                else:
                    l = m+1
        return -1