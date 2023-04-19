class Solution:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    You can return the answer in any order
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result_dict = dict()
        for i, value in enumerate(nums):
            remaining_value = target - nums[i]

            if remaining_value in result_dict:
                return [i, result_dict[remaining_value]]

            result_dict[value] = i