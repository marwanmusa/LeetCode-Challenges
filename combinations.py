from typing import List

class Solution:
    """
    Task:
    Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
    You may return the answer in any order.
    """
    # Method 1 - Batracking
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        backtrack(1, [])
        return res

    # Method 2
    def combine(self, n: int, k: int) -> List[List[int]]:
        vals = []
        def helper(cands, nums):
            l = len(nums)
			# If we've filled our current list of nums append.
            if l == k:
                vals.append(nums)
                return
			# If we have enough numbers left to fill our current list, proceed.
            if len(cands) >= k-l:
			    # for candidates left call our func. recursively
				# incrementing cands and adding cands[i] to our nums.
                for i in range(len(cands)):
                    helper(cands[i+1:], nums + [cands[i]])
        helper(range(1, n+1), [])
        return vals