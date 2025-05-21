import collections

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        d = collections.Counter(nums)
        res = 0
        for k in d:
            if d.get(k+1):
                res = max(res, d[k] + d[k+1])
        return res
    

    # shorter
    def findLHS(self, nums: list[int]) -> int:
        d = collections.Counter(nums)
        return max((d[k] + d[k+1] if d.get(k+1) else 0 for k in d), default=0)
