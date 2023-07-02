from typing import List

class Solution:
    """
    Task:
    You are given a large integer represented as an integer array digits,
    where each digits[i] is the ith digit of the integer.
    The digits are ordered from most significant to least significant
    in left-to-right order. The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.
    """
    # Approach digit to int, int to digit
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        idx = 0

        # arr digits to int form
        digitsToInt = 0
        for i in reversed(range(n)):
            digitsToInt += digits[idx] * (10 ** (i))
            idx += 1

        # add 1 to digit int form
        digitsToInt += 1

        # int digits to arr form
        digits.clear()
        while digitsToInt:
            digitsToInt, remainder = divmod(digitsToInt, 10)
            digits.insert(0, remainder)
        return digits


    # Approach: when digit is 9 -> 0 add [1] to digits
    # if digit < 9 just add 1 return digits
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, d in reversed(list(enumerate(digits))):
            if d < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits


    # Using string representation
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(int(x) for x in str(int("".join(str(num) for num in digits))+1))