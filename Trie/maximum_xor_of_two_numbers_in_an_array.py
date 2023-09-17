"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.
"""

from itertools import combinations as comb

class Solution:
    # Approach 1: Brute Force / will give TLE
    def findMaximumXOR(self, nums: list[int]) -> int:
        x = 0
        for pair in comb(nums, 2):
            a, b = pair
            x = max(a^b, x)
        return x