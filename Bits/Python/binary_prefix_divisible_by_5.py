class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        res = [not nums[0]]
        cur = nums[0]
        n = len(nums)
        if n > 1:
            for i in range(1, n):
                cur = cur * 2 + nums[i]
                res.append(not cur % 5)
        return res

    # shorter
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        cur, nums[0] = nums[0], nums[0] == 0
        for i in range(1, len(nums)):
            cur = (cur * 2 + nums[i]) % 5
            nums[i] = not cur
        return nums
