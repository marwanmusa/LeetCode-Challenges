from typing import List

class Solution:
    """
    Task:
    You are given an m x n integer grid accounts where accounts[i][j] is the amount of money
    the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
    Return the wealth that the richest customer has.

    A customer's wealth is the amount of money they have in all their bank accounts.
    The richest customer is the customer that has the maximum wealth.
    """
    # method 1
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            max_wealth = max(max_wealth, sum(account))
        return max_wealth

    # method 2
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            cur_account_wealth = 0
            for balance in account:
                cur_account_wealth += balance
            max_wealth = max(max_wealth, cur_account_wealth)
        return max_wealth