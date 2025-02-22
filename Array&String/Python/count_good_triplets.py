class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        cnt, n = 0, len(arr)
        for i in range(n-2):
            for j in range(i+1, n-1):
                a_ = abs(arr[i] - arr[j])
                if a_ > a: continue
                for k in range(j+1, n):
                    b_, c_ =  abs(arr[j] - arr[k]), abs(arr[i] - arr[k])
                    if b_ > b or c_ > c: continue
                    if a_ <= a and b_ <= b and c_ <= c: cnt += 1
        return cnt