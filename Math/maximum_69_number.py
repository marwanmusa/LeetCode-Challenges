import collections

class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = collections.deque()
        while num:
            rem = num % 10
            num //= 10
            nums.appendleft(rem)
        flip = False
        pows = len(nums) - 1
        ans = 0
        for i, x in enumerate(nums):
            if x != 9 and not flip:
                nums[i] = 9
                flip = True
            ans += nums[i] * (10 ** pows)
            pows -= 1
        return ans
