class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        return [True if x+extraCandies > max(candies)-1 else False for x in candies]