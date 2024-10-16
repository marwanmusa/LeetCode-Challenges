class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        sum_arr = sum(arr)
        if sum_arr % 3: return False
        if all(v == 0 for v in arr): return True
        part_n, cur = 3, 0
        for i in range(len(arr)):
            cur += arr[i]
            if part_n == 1 and i < len(arr) - 1:
                continue
            if cur == (sum_arr // 3):
                cur = 0
                part_n -= 1
        return part_n == 0