class Solution:
    """
    Task:
    Given an integer n, return true if it is a power of three. Otherwise, return false.

    An integer n is a power of three, if there exists an integer x such that n == 3x.
    """
    # Method 1
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0: return False
        if n == 1: return True
        if n > 1: return n%3 == 0 and self.isPowerOfThree(n/3)
        else: return False


    # Method 2
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return True if n == 1 else False