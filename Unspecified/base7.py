class Solution:
    """
    Task:
        Given an integer num, return a string of its base 7 representation.
    """
    def convertToBase7(self, num: int) -> str:
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n //= 7
        return '-' * (num < 0) + res or '0'

    # recursive approach
    def convertToBase7(self, n: int) :
        if n < 0: return '-' + self.convertToBase7(-n)
        if n < 7: return str(n)
        return self.convertToBase7(n // 7) + str(n % 7)

    # longer version of recursive
    def convertToBase7(self, num: int) :
        if num < 0:
            return f"-{self.convertToBase7(-num)}"
        elif num < 7:
            return str(num)
        res = ""
        while num > 0:
            num, r = divmod(num, 7)
            res += str(r)
        return res[::-1]
