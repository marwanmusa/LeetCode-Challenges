class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            a, b, c = nums[i], nums[i-1], nums[i-2]
            if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
                ans = max(ans, a+b+c)
        return ans