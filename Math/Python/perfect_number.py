class Solution:
    # TLE Solution
    def checkPerfectNumber(self, num: int) -> bool:
        divs = [n for n in range(1, num//2 + 1) if num % n == 0]
        return sum(divs) == num


    # perfect Number exist until 10^8 (only 5)
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6,28,496,8128,33550336]
    
    # brute-force approach
    def checkPerfectNumber(self, num: int) -> bool:
        ans = 1
        if num == 1: return False
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                ans += i + num // i
        return ans == num