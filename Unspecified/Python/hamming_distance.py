class Solution:
    """
    Task:
    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

    Given two integers x and y, return the Hamming distance between them.
    """
    # Method 1
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance

    # Method 2
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')