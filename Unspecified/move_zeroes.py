class Solution:
    """
    Task:
    Given an integer array nums, move all 0's to the end of it
    while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.
    """
    # O(N) time complexity
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                print(f"nums[i] {nums[i]}, nums[j] {nums[j]}")
                nums[i], nums[j] = nums[j], nums[i]
                j += 1