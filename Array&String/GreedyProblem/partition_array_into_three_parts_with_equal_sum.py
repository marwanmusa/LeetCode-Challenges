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

    # shorter
    def canThreePartsEqualSum(self, A: list[int]) -> bool:
        average, remainder, part, cnt = sum(A) // 3, sum(A) % 3, 0, 0
        for a in A:
            part += a
            if part == average:
                cnt += 1
                part = 0
        return not remainder and cnt >= 3

    # greedy pointers
    def canThreePartsEqualSum(self, A: list[int]) -> bool:
        l, r, s = 1, len(A) - 2, sum(A)
        if s % 3 != 0:
            return False
        leftSum, rightSum, average = A[0], A[-1], s // 3
        while l <= r:
            if l < r and leftSum != average:
                leftSum += A[l]
                l += 1
            if l < r and rightSum != average:
                rightSum += A[r]
                r -= 1
            if leftSum == average == rightSum:
                return True
            if l == r:
                return False
        return False