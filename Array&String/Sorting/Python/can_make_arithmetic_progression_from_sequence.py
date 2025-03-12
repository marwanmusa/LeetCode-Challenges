class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        n = len(arr)
        if n == 2: return True
        for i in range(2, n):
            if arr[i] - arr[i-1] != diff: return False
        return True