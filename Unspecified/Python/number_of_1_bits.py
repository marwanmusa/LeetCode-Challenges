class Solution:
    """
    Task:
    Write a function that takes the binary representation of an unsigned integer and
    returns the number of '1' bits it has (also known as the Hamming weight).
    """
    # Method 1, sum all 1 bits in arr after converting to binary representation
    def hammingWeight(self, n: int) -> int:
        return sum([int(x) for x in bin(n)[2:]])

    # Method 2, using bitwise and recursion
    def hammingWeight(self, n: int) -> int:
        return 0 if n == 0 else (n & 1) + self.hammingWeight(n >> 1)