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