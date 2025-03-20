class Solution:
    """
    Task:
    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
    """
    # Brute-force approach
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1 / self.myPow(x, -n)
        return x * self.myPow(x, n-1)


    # recursive binary exponentiation
    def myPow(self, x: float, n: int) -> float:
        """
        Instead of reducing the exponent nnn by 1 at each recursive call
        like in the brute-force method,we will reduce it by half here.
        Thus, instead of linear steps, it will take us logarithmic steps
        to perform all the multiplications.
        """
        def binaryExp(x, n):
            if n == 0: return 1.0
            if n < 0: return 1.0 / binaryExp(x, -n)

            # Binary exponentiation steps.
            if n % 2 == 1: return x * binaryExp(x * x, (n - 1) / 2)
            else: return binaryExp(x * x, n / 2)
        return binaryExp(x, n)