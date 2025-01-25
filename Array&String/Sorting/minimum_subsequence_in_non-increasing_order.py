class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nums = sorted(nums)
        tot = sum(nums)

        s = 0
        ans = []
        for i in range(n - 1, -1, -1):
            s += nums[i]
            ans.append(nums[i])
            if s > (tot - s):
                return ans
