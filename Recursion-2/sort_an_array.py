class Solution:
    """
    Given an array of integers nums, sort the array in ascending order and return it.

    You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
    and with the smallest space complexity possible.
    """
    # Using merge sort
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        
        mid = int(len(nums)/2)
        l_nums = self.sortArray(nums[:mid])
        r_nums = self.sortArray(nums[mid:])
        
        def merge(l:list, r:list) -> list:
            ptr_l = ptr_r = 0
            ans = []
            while ptr_l < len(l) and ptr_r < len(r):
                if l[ptr_l] < r[ptr_r]:
                    ans.append(l[ptr_l])
                    ptr_l += 1
                else:
                    ans.append(r[ptr_r])
                    ptr_r += 1
            ans.extend(l[ptr_l:])
            ans.extend(r[ptr_r:])
            return ans
        
        return merge(l_nums, r_nums)
    