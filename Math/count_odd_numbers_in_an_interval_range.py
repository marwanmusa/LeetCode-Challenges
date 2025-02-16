class Solution:
    def countOdds(self, l: int, h: int) -> int:
        nums = h - l + 1
        isOdd, lIsOdd = nums & 1, l & 1
        halfN = nums//2
        if isOdd and lIsOdd: return halfN + 1
        return halfN
