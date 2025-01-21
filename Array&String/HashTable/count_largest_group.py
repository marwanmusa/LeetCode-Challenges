from collections import defaultdict

class Solution:
    def sumDigits(self, n: int) -> int:
        ans = 0
        while n:
            ans += n % 10
            n //= 10
        return ans

    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        maxd = 0
        for i in range(1, n+1):
            sd = self.sumDigits(i)
            d[sd] += 1
            maxd = max(maxd, d[sd])
        res = 0
        for k in d:
            if d[k] == maxd: res += 1
        return res
