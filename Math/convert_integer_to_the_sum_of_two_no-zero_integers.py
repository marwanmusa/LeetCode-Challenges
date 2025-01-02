class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for i in range(1, n+1):
            if self.check(i) and self.check(n-i):
                return [i, n-i]
        return []


    def check(self, n):
        while n:
            if not n & 1:
                nNext = n // 10
                if (n - (10 * nNext) == 0):
                    return False
                n = nNext
            n //= 10
        return True
