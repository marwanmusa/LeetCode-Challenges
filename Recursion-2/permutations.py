from typing import List

class Solution:
    """
    Task:
    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.
    """
    # Method 1 - backtracking
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # base case
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res

    # method 2 - algoritma by itertools
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(self.permutations(nums))

    def permutations(self, elements):
        if len(elements) <= 1:
            yield elements
            return
        for perm in self.permutations(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

    # method 2 -> make it in 1 function
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(elements):
            if len(elements) <= 1:
                yield elements
                return
            for perm in helper(elements[1:]):
                for i in range(len(elements)):
                    yield perm[:i] + elements[0:1] + perm[i:]
        return list(helper(nums))
    
    # another approach
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
        res = []
        for i in range(len(nums)):
            sub = nums[:i] + nums[i+1:]
            for p in self.permute(sub):
                res.append([nums[i]] + p)
        return res
    
    # Method 3 - recursion with bactracking
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(nums, perm=[], res=[]):
            if not nums: res.append(perm)
            for i in range(len(nums)):
                sub = nums[:i] + nums [i+1:]
                perm.append(nums[i])
                recursive(sub, perm, res)
                perm.pop()
            return res
        return recursive(nums)
    
    # Method 3 - recursion without bactracking
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(nums, perm=[], res=[]):
            if not nums: res.append(perm)
            for i in range(len(nums)):
                recursive(nums[:i] + nums[i+1:], perm + [nums[i]], res)
            return res
        return recursive(nums)
    