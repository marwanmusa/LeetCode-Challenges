class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        if len(nums) == 0:
            return nums
        writeIdx = 0
        for readIdx in range(len(nums)):
            if nums[readIdx] % 2 == 0:
                nums[readIdx], nums[writeIdx] = nums[writeIdx], nums[readIdx]
                writeIdx += 1
        j = 1
        for i in range(len(nums)):
            if nums[i] & 1:
                nums[i], nums[j] = nums[j], nums[i]
                j += 2
        return nums
    
    # Method 2
    def sortArrayByParityII(self, a):
        i = 0 # pointer for even misplaced
        j = 1 # pointer for odd misplaced
        sz = len(a)
        
        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens

        while i < sz and j < sz:
            if a[i] % 2 == 0:
                i += 2
            elif a[j] % 2 == 1:
                j += 2
            else:
                # a[i] % 2 == 1 AND a[j] % 2 == 0
                a[i],a[j] = a[j],a[i]
                i += 2
                j += 2

        return a