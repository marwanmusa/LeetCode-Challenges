class Solution:
    """
    Task:
    The complement of an integer is the integer you get when you flip all the 0's to 1's
    and all the 1's to 0's in its binary representation.

    For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
    Given an integer num, return its complement.
    """
    def findComplement(self, num: int) -> int:
        bits = {'0':'1', '1':'0'}
        revs = ""
        for bit in bin(num)[2:]:
            revs += bits[bit]
        return int(revs, 2)
    
    # flip bit by bit
    def findComplement(self, num: int) -> int:
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num
    
    # Find the bit length (say L) and flip num by num ^ 11...1 (L ones).
    def findComplement(self, num: int) -> int:
        return num ^ ((1 << num.bit_length()) - 1)
    
    # same with prev approach but a little bit different
    def findComplement(self, num: int) -> int:
        return num ^ ((1 << len(bin(num)) - 2) - 1)
    
    # Flip num first then get the last L bits
    def findComplement(self, num: int) -> int:
        return ~num & ((1 << num.bit_length()) - 1)