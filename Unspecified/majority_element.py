class Solution:
    """
    Task:
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

    Follow-up: Could you solve the problem in linear time and in O(1) space?
    """
    def majorityElement(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums)//2]