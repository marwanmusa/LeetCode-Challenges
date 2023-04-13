from typing import List

class Solution:
    """
    Task:
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

    Follow up:
    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
    """
    # Method 1
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums.pop())

    # Method 2
    def rotate(self, nums: List[int], k: int) -> None:
        break_idx = (len(nums) - k) % len(nums)
        nums[:] = nums[break_idx:] + nums[:break_idx]

    # Method 3
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k > 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

    # Method 4
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]