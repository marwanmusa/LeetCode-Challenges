from collections import defaultdict

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        limit = len(arr) // 4
        mp = defaultdict(int)
        for n in arr:
            mp[n] += 1
            if mp[n] > limit: return n
        return -1

    # memory efficient implementation
    def findSpecialInteger(self, arr: list[int]) -> int:
        limit = len(arr) // 4
        count, special = 1, arr[0]
        for i in range(1, len(arr)):
            if arr[i] == special: count += 1
            else: count = 1
            if count > limit: return special
            special = arr[i]
        return special