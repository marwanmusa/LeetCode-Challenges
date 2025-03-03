from typing import List

class Solution:
    """
    Task:
    Given an array of integers arr, return true if and only if it is a valid mountain array.
    Recall that arr is a mountain array if and only if:
        - arr.length >= 3
        - There exists some i with 0 < i < arr.length - 1 such that:
            - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
            - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    """
    def validMountainArray(self, arr: List[int]) -> bool:
        if (len(arr) < 3) or (arr[0] > arr[1]) or (arr[-2] < arr[-1]):
            return False
        hills, valleys = set(), set()
        idx = 0
        max_ = -1
        for n in arr:
            if max_ > n:
                break
            if n in hills:
                return False
            hills.add(n)
            max_ = max(max_, n)
            idx += 1
        min_ = max_
        for i in range(idx, len(arr)):
            if arr[i] in valleys or min_ < arr[i]:
                return False
            valleys.add(arr[i])
            min_ = min(min_, arr[i])
        return True

    # More efficient way
    def validMountainArray(self, arr: List[int]) -> bool:
        l,j = 0,len(arr)-1
        n = len(arr)
        while l+1 < n and arr[l] < arr[l+1]:
            l += 1
        while j > 0 and arr[j] < arr[j-1]:
            j -= 1
        return 0 < l == j < n-1