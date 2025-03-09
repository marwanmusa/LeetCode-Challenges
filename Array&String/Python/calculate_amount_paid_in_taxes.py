class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        ans, prev = 0, 0
        for up, pct in brackets:
            ans += (min(up - prev, income) * (pct/100))
            income -= (up - prev)
            prev = up
            if income < 0: break
        return ans