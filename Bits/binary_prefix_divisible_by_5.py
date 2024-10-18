class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        res = [nums[0] % 5 == 0]
        cur = nums[0]
        n = len(nums)
        if n > 1:
            for i in range(1, n):
                temp = (2**i) + nums[i]
                cur += temp
                res.append(cur % 5 == 0)
        return res