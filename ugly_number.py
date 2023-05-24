class Solution:
    """
    Task:
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return true if n is an ugly number.
    """
    def isUgly(self, n: int) -> bool:
        # A non-positive integer cannot be ugly
        if n <= 0: return False

        # Factorize by dividing with permitted factors
        for divisor in [2, 3, 5]:
            print(n, divisor)
            n = self.keep_dividing_when_divisible(n, divisor)

        # Check if the integer is reduced to 1 or not.
        return n == 1

    # Keep dividing dividend by divisor when division is possible
    def keep_dividing_when_divisible(self, dividend: int, divisor: int):
        while dividend % divisor == 0:
            dividend //= divisor
        return dividend