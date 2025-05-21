from collections import Counter
from typing import List
# 1636. Sort Array by Increasing Frequency
# https://leetcode.com/problems/sort-array-by-increasing-frequency/
# Given an array of integers nums, sort the array in increasing order based on the frequency of the values.

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        freqToNums = {}
        for num, freq in freq.items():
            freqToNums[freq] = freqToNums.get(freq, []) + [num]

        res = []
        for f in sorted(freqToNums.keys()):
            numsAtFreq = sorted(freqToNums[f], reverse=True)
            for num in numsAtFreq: res.extend([num] * f)
        return res

    # using sort + lambda function
    def frequencySort2(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
