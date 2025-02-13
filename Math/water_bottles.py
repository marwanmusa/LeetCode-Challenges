class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            rem, div = numBottles % numExchange, numBottles // numExchange
            ans += div
            numBottles = rem + div
        return ans