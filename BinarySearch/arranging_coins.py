from bisect import bisect_left

class Solution:
    """
    Task:
    You have n coins and you want to build a staircase with these coins.
    The staircase consists of k rows where the ith row has exactly i coins.
    The last row of the staircase may be incomplete.

    Given the integer n, return the number of complete rows of the staircase you will build.
    """
    def arrangeCoins(self, n: int) -> int:
        res = 0
        if n == 1: return 1
        for i in range(1, n):
            if n - i < 0:
                return res
            n -= i
            res += 1
        return res
    
    
    def arrangeCoins(self, n: int) -> int:
        s, i = 0, 1
        while n >= i:
            n -= i
            s += 1
            i += 1
        return s


    # using math analysis
    def arrangeCoins(self, n: int) -> int:
        return int((2*n + 0.25)**0.5 - 0.5)
        # or
        # return int(((8*n+1)**0.5)/2 - 0.5)
    
    # binary search
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            one_step = mid * (mid + 1) // 2
            if one_step == n:
                return mid
            elif one_step > n:
                right = mid - 1
            else:
                left = mid + 1
        return right
    
    # using bisect
    def arrangeCoins(self, n: int) -> int:
        res = bisect_left(range(1, n), n, key = lambda x: x*(x+1)//2) + 1 
        if res*(res+1)//2 == n:
            return res
        return res-1
    

