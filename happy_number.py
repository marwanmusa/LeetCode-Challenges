class Solution:
    """
    Task:
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:
    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay),
      or it loops endlessly in a cycle which does not include 1.
    - Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.
    """
    # Method 1 using list to calculate sum of square each digit
    def isHappy(self, n: int) -> bool:
        s = set()
        s.add(n)
        while True:
            if n == 1 or n == 7:
                return True
            n = self.sumDigitSquare(n)
            if n in s:
                return False
            s.add(n)
        return False

    # Method 2 using list loop modulo and division to calculate sum of square each digit
    def isHappy(self, n: int) -> bool:
        s = set()
        s.add(n)
        while True:
            if n == 1 or n == 7:
                return True
            n = self.sumDigitSquare(n)
            if n in s:
                return False
            s.add(n)
        return False

    def sumDigitSquare(self, n):
        sq = 0
        while n!=0:
            digit = n % 10
            sq += digit*digit
            n //= 10
        return sq