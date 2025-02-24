class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3: return False
        for i in range(n-2):
            if all(map(lambda x: x & 1, arr[i : i+3])): return True
        return False
