class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        cur, idx, n = 1, 0, len(arr)
        while True:
            if cur != arr[idx]: k -= 1
            if cur == arr[idx] and idx < n-1: idx += 1
            if k == 0: break
            cur += 1
        return cur
    
    # binary search
    def findKthPositive_bs(self, arr: list[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] - m - 1 < k: l = m + 1
            else: r = m
        return l + k