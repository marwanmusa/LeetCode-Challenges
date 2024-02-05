import sys
sys.set_int_max_str_digits(0)

class Solution:
    """
    Task:
    Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

    You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
    You must also not convert the inputs to integers directly.
    """
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        a = b = 0
        for i in range(l1):
            r = ord(num1[i]) - 48
            a = a*10 + r
        for i in range(l2):
            s = ord(num2[i]) - 48
            b = b*10 + s
        return str(a + b)