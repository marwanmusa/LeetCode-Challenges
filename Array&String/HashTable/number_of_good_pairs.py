from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]: ans += 1
        return ans

    # shorter
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = Counter(nums)
        return sum(v * (v - 1) // 2 for v in count.values())