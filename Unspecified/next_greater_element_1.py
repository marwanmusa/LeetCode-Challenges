class Solution:
    """
    Task:
    The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
    You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

    For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
    and determine the next greater element of nums2[j] in nums2. If there is no next greater element,
    then the answer for this query is -1.

    Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
    """
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        idx = {num : i for i, num in enumerate(nums2)}
        ans = []
        for el in nums1:
            if any(i > el for i in nums2[idx[el]:]):
                ans.append(next(i for i in nums2[idx[el]:] if i > el))
            else:
                ans.append(-1)
        return ans
    
    # using stacking
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m, stk = {}, []
        for v in nums2:
            while stk and stk[-1]:
                m[stk.pop()] = v
            stk.append(v)
        return [m.get(v, -1) for v in nums1]