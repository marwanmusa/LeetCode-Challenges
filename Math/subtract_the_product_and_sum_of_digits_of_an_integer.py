class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mult, adds = 1, 0
        while n > 0:
            cur = n % 10
            mult *= cur
            adds += cur
            n //= 10
        return mult - adds