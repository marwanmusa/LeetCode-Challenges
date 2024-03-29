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

    # Approach 2: Bit Operation
    def findMaximumXOR(self, nums: list[int]) -> int:
        ans = 0
        for i in range(32)[::-1]:
            ans <<= 1
            prefixes = {num >> i for num in nums}
            ans += any(ans^1 ^ p in prefixes for p in prefixes)
        return ans

    # Approach 2: Modification I
    def findMaximumXOR(self, nums: list[int]) -> int:
        ans = 0
        for i in reversed(range(32)):
            prefixes = set([x >> i for x in nums])
            ans <<= 1
            candidate = ans + 1
            if any(candidate^p in prefixes for p in prefixes):
                ans = candidate
        return ans
    
    # Approach 2: Modification 2 - more readable
    def findMaximumXOR(self, nums: list[int]) -> int:
        ans = 0
        for i in reversed(range(32)):
            prefixes = set([x >> i for x in nums])
            ans <<= 1
            candidate = ans + 1
            for p in prefixes:
                if candidate ^ p in prefixes:
                    ans = candidate
                    break
        return ans