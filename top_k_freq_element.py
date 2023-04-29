from collections import Counter
from typing import List
import heapq

class Solution:
    """
    Task:
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.
    """
    # Approach 1 : Heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)