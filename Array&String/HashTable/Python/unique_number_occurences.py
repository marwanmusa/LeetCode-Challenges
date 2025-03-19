from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr = Counter(arr)
        return len(arr) == len(set(arr.values()))