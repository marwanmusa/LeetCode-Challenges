class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        inc = True
        dec = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]: inc = False
            if nums[i] > nums[i-1]: dec = False
        return inc or dec
    
    # unfamiliar way
    def isMonotonic(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                break
        else:
            return True
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                break
        else:
            return True
        return False
    
    # one-liner
    def isMonotonic(self, nums: list[int]) -> bool:
        return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))