class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        sum_arr = sum(arr)
        if sum_arr % 3: return False
        if all(v == 0 for v in arr): return True
        part_n, cur = 3, arr[0]
        for i in range(1, len(arr)):
            cur += arr[i]
            if cur == (sum_arr // 3):
                cur = 0
                part_n -= 1
        return part_n == 0