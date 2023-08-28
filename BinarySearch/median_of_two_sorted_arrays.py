from typing import List

class Solution:
    """
    Task:
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
    """
    # Approach 1: Merge Sort
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        size = m + n
        p1, p2 = 0, 0
        
        # Get the smaller value between nums1[p1] and nums2[p2].
        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans
        
        if size & 1:
            for _ in range((m + n) // 2):
                _ = get_min()
            return get_min()
        else:
            for _ in range((m + n) // 2 - 1):
                _ = get_min()
            return (get_min() + get_min()) / 2
