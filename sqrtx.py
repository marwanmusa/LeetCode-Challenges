class Solution:
    """
    Task:
        Given a non-negative integer x,
        return the square root of x rounded down to the nearest integer.
        The returned integer should be non-negative as well.

        You must not use any built-in exponent function or operator.

        For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
    """
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        ans = x
        while lo <= hi:
            mid = int(lo + (hi - lo)/2)
            if (mid * mid) == x:
                return mid
            elif (mid * mid) > x:
                hi = mid - 1
            else:
                ans = mid
                lo = mid + 1
        return ans