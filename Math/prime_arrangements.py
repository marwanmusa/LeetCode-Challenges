class Solution:
    def SieveOfEratosthenes(self, n: int):
        prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        cnt = 0
        for p in range(2, n+1):
            if prime[p]: cnt += 1
        return cnt


    def factorial(self, n: int) -> int:
        res = 1
        while n:
            res *= n
            n -= 1
        return res

    def numPrimeArrangements(self, n: int) -> int:
        divisor = (10 ** 9) + 7
        primes = self.SieveOfEratosthenes(n)
        composites = n - primes
        return (self.factorial(primes) * self.factorial(composites)) % divisor