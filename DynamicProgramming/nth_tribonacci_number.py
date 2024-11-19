class Solution:
    def tribonacci(self, n: int) -> int:
        fn = [0] * 38
        fn[0] = 0
        fn[1] = 1
        fn[2] = 1
        if n < 3: return fn[n]
        for i in range(3, 38):
            fn[i] = fn[i-1] + fn[i-2] + fn[i-3]
            if i == n:
                return fn[n]
