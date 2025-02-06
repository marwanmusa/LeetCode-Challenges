import math
from collections import defaultdict

class Solution:
    def factorial(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            dp[i] = i * dp[i-1]
        return dp[n]

    def combination_product(self, n, k):
        "n len(array), k sublist to select"
        if n < k: return 0
        return self.factorial(n) // (self.factorial(k) * self.factorial(n - k))

    def tupleSameProduct(self, nums: list[int]) -> int:
        prod, ans = defaultdict(int), 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                mult = nums[i] * nums[j]
                prod[mult] += 1
        for k in prod:
            if prod[k] >= 2: ans += self.combination_product(prod[k]) * 8
        return ans


    # shorter version, using built-in funcs
    def tupleSameProduct(self, nums: list[int]) -> int:
        prod, ans = defaultdict(int), 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                mult = nums[i] * nums[j]
                prod[mult] += 1
        return sum(math.comb(v, 2) * 8 for v in prod.values() if v >= 2)