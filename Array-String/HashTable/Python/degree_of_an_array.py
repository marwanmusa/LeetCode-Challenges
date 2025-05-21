class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        freq, first, last = {}, {}, {}
        for i, n in enumerate(nums):
            freq[n] = freq.get(n, 0) + 1
            if n not in first: first[n] = i
            last[n] = i
        minLen, degree = len(nums), 0
        for n, count in freq.items():
            if count > degree:
                degree = count
                minLen = last[n] - first[n] + 1
            elif count == degree:
                minLen = min(last[n] - first[n] + 1, minLen)
        return minLen