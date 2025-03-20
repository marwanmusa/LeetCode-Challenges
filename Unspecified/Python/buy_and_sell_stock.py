class Solution:
    """
    Task:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
    in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """
    # first method - time limit exceed
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                cur_diff = prices[j]-prices[i]
                if cur_diff > diff:
                    diff = cur_diff
        return diff

    # second method - `Accepted`
    def maxProfit(self, prices: List[int]) -> int:
        max_ = 0
        min_ = prices[0]
        for i in range(len(prices)):
            min_ = min(min_, prices[i])
            max_ = max(max_, prices[i] - min_)
        return max_