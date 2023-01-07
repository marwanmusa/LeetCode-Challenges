class Solution:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    You can return the answer in any order

    Constraints :
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if 2 <= len(nums) <= 10**4: # Constraint
            if (-10)**9 <= target <= 10**9: # Constraint
                result_dict = dict()
                for i, value in enumerate(nums):
                    if (-10)**9 <= nums[i] <= 10**9: # Constraint
                        remaining_value = target - nums[i]

                        if remaining_value in result_dict:
                            return [i, result_dict[remaining_value]]

                        result_dict[value] = i