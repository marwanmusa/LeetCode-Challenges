import math

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        if len(nums) == 3:
            return math.prod(nums)
        all_max = []
        for i in range(3):
            x = max(nums)
            nums.remove(x)
            all_max.append(x)
        return math.prod(all_max)