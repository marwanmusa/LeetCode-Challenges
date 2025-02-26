import math
import heapq

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        if len(nums) == 3:
            return math.prod(nums)
        all_max = []
        min_neg = []
        all_neg = [x for x in nums if x < 0]
        if len(all_neg) >= 2:
            for i in range(2):
                x = min(all_neg)
                all_neg.remove(x)
                min_neg.append(x)
        arr = nums[::]
        for i in range(3):
            x = max(arr)
            arr.remove(x)
            all_max.append(x)
        return max(math.prod(all_max), math.prod(min_neg)*max(nums)) if min_neg else math.prod(all_max) 
    

    def maximumProduct(self, nums: list[int]) -> int:
        bigs = heapq.nlargest(3, nums)
        smalls = heapq.nsmallest(2, nums)
        return max(math.prod(bigs), math.prod(smalls)*max(bigs))
    

    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(math.prod(nums[-3:]), math.prod(nums[:2])*nums[-1])