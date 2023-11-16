from itertools import combinations as comb
class Solution:
    """
    Task:
    Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

    You may return the answer in any order.
    """
    # using python built-in method
    def combine(self, n: int, k: int) -> list[list[int]]:
        return list(comb(range(1, n+1), k))
    
    # using recursive approach
    def combine(self, n: int, k: int) -> list[list[int]]:
        if k == 0 or n < k:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]