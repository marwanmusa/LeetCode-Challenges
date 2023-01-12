class Solution:
    """
    Task:
    Given an integer x, return true if x is a `palindrome`, and false otherwise.
    """
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            num = x
            reversed_num = 0

            while num != 0:
                digit = num % 10
                reversed_num = reversed_num * 10 + digit
                num //= 10
            return x == reversed_num
        else:
            return False