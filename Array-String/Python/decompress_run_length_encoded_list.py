class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        n, ans, i = len(nums), [], 0
        while i < n-1:
            freq, val = nums[i], nums[i+1]
            ans.extend([val]*freq)
            i += 2
        return ans
