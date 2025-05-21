from typing import List

class Solution:
    # O(1) space solution without sorting
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing, duplicate, size = -1, -1, len(nums)

        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0: duplicate = abs(n)
            else: nums[idx] *= -1

        for i in range(size):
            if nums[i] > 0:
                missing = i + 1
                break

        return [duplicate, missing]
