class Solution:
    #1 finding the repeated 0 or 1 in bit string n
    def hasAlternatingBits(self, n: int) -> bool:
        return '11' not in bin(n) and '00' not in bin(n)
