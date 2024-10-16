class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        sums, n = sum(arr), len(arr)
        mod, rem = sums % 3, sums // 3
        if mod: return False
        if not any(arr): return True
        part_n, cur = 3, 0
        for i in range(n):
            cur += arr[i]
            if part_n == 1 and i < n - 1: continue
            if cur == rem:
                cur = 0
                part_n -= 1
        return part_n == 0