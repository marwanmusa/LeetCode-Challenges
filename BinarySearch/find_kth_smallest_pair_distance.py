from typing import List
from heapq import heappop, heappush, heapify
class Solution:
    """
    Task:
    The distance of a pair of integers a and b is defined as the absolute difference between a and b.

    Given an integer array nums and an integer k, return the kth smallest distance among all the pairs
    nums[i] and nums[j] where 0 <= i < j < nums.length.
    """
    # Approach 1: Heap [Time limit exceeded]
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        heap = [(nums[i+1] - nums[i], i, i+1) for i in range(n-1)]
        heapify(heap)
        for _ in range(k):
            d , root, nei = heappop(heap)
            if nei+1 < n:
                heappush(heap, (nums[nei+1] - nums[root], root, nei+1))
        return d
    
    # Approach 2: Binary Search + Prefix Sum
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            return sum(prefix[min(x + guess, W)] - prefix[x] + multiplicity[i]
                       for i, x in enumerate(nums)) >= k
        
        nums.sort()
        W = nums[-1]

        # multiplicity[i] = number of nums[j] == nums[i] (j < i)
        multiplicity  = [0] * len(nums)
        for i, x in enumerate(nums):
            if i and x == nums[i-1]:
                multiplicity[i] = 1 + multiplicity[i-1]
        
        # prefix[v] = number of values <= v
        prefix = [0] * (W + 1)
        l = 0
        for i in range(len(prefix)):
            while l < len(nums) and nums[l] == i:
                l += 1
            prefix[i] = l

        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = lo + (hi-lo)//2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo