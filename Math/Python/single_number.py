from functools import reduce


class Solution:
    """
    Task:
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and use only constant extra space.

    we'll solve this using xor ^
    - xor is commutative: A ^ B = B ^ A
    - xor is associative: (A ^ B) ^ C = A ^ (B ^ C)
    - xoring with zero does nothing: A ^ 0 = A
    - xoring something twice removes it: A ^ A = 0
    """
    # firs method using loop
    def singleNumber(self, nums: list[int]) -> int:
        x = nums[0]
        for i in range(1, len(nums)):
            x = x ^ nums[i]
        return x

    # method 2 using reduce form functools lib
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x^y, nums)