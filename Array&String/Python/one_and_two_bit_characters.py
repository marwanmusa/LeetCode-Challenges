class Solution:
    """
    Task:
    We have two special characters:
        The first character can be represented by one bit 0.
        The second character can be represented by two bits (10 or 11).
        Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
    """
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n = len(bits)
        if bits[-1] == 1: return False
        i = 0
        while i < n:
            if bits[i] == 1:
                i += 2
                if i == n: return False
            elif bits[i] == 0:
                i += 1
        return True
    
    # shorter version
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n, i = len(bits), 0
        while i < n-1:
            if bits[i] == 1: i += 2
            else: i += 1
        return i == n-1