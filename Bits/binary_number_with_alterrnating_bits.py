class Solution:
    #1 finding the repeated 0 or 1 in bit string n
    def hasAlternatingBits(self, n: int) -> bool:
        return '11' not in bin(n) and '00' not in bin(n)

    #2 manually check
    def hasAlternatingBits(self, n: int) -> bool:
        last = n % 2
        n //= 2
        while n > 0:
            cur = n % 2
            if last == cur:
                return False
            last = cur
            n //= 2
        return True
    
    # check bitwise AND of n with (n>>1)
    def hasAlternatingBits(self, n: int) -> bool:
        return (n and (n>>1)) == 0 if n > 1 else False