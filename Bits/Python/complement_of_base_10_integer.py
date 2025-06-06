from functools import reduce

class Solution:
    # Solution 1
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        bins = reversed([(x+1) % 2 for x in map(int, bin(n)[2:])])
        return sum(x * (2 ** i) for i, x in enumerate(bins))

    # Solution 2
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        bins = [(x+1) % 2 for x in map(int, bin(n)[2:])]
        return reduce(lambda x, y: (2 * x) + y, bins)

    # Solution 3 using shift operator
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        bins = [(x+1) % 2 for x in map(int, bin(n)[2:])]
        res = 0
        for x in bins:
            res = (res << 1) | x
        return res

    # masking
    def bitwiseComplement(self, n: int) -> int:
        cnt, ans = 0, 0
        if n==0: return 1
        while n>0:
            if not n & 1:
                ans =ans +(2**cnt)
            cnt +=1
            n >>= 1
        return ans