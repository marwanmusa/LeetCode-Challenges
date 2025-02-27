class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        freq = [0] * 10001
        for n in nums:
            freq[n] += 1
            if freq[n] == len(nums) // 2: return n
        return -1