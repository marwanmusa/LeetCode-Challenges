class Solution:
    """
    Task:
    Given an integer array nums sorted in non-decreasing order,
    return an array of the squares of each number sorted in non-decreasing order.

    Follow up: Squaring each element and sorting the new array is very trivial,
    could you find an O(n) solution using a different approach?
    """
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res_arr = [0]*len(nums)
        l = 0
        r = len(nums) - 1
        for i in reversed(range(len(nums))):
            left_val = nums[l]
            right_val = nums[r]

            if abs(left_val) > abs(right_val):
                res_arr[i] = left_val * left_val
                l += 1
            else:
                res_arr[i] = right_val * right_val
                r -= 1
        return res_arr