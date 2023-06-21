class Solution:
    """
    Task:
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
    such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    """
    # fibonacci func without memoization
    def fib(self, n):
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

    """
    In order to obtain the result for f(n), we would need to calculate the number f(n-2) twice,
    since f(n-1) = f(n-2)*f(n-3) and so on. Then, there will be so many duplicate calculation.

    To eliminate the duplicate calculation in the above case, one of the ideas would be to store
    the intermediate results in the cache so that we could reuse them later without recalculation.
    """

    # with memoization
    def fib(self, n):
        cache = {}
        def recur_fib(n):
            if n in cache:
                return cache[n]
            if n < 2:
                result = n
            else:
                result = recur_fib(n-1) + recur_fib(n-2)
            cache[n] = result
            return result
        return recur_fib(n)
