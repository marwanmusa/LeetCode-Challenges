class Solution:
    # TLE Solution
    def checkPerfectNumber(self, num: int) -> bool:
        divs = [n for n in range(1, num//2 + 1) if num % n == 0]
        return sum(divs) == num
