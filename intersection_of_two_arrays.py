class Solution:
    """
    Task:
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must appear as many times as it shows in both arrays and
    you may return the result in any order.
    """
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Solution 1 : Sorting and two-pointer approach
        nums1.sort()
        nums2.sort()
        intersection = []
        m,n = len(nums1),len(nums2)
        i,j = 0,0
        while i<m and j<n:
            if nums1[i] == nums2[j]:
                if nums1[i] not in intersection:
                    intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return intersection


"""
Follow up:
1. What if the given array is already sorted? How would you optimize your algorithm?
ans: If the given arrays are sorted, we can use a two-pointer approach. At each step,
we compare one element of A with one element of B. If both are equal, we add it to the list,
else we move forward.

2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
ans: We can make a hash table of the smaller array(nums2) so that our searching
becomes faster and all elements appear only once. Now for each element of the bigger array(nums1),
we can perform a search operation of that element in the hash table.
The search operation in a hash table is, in an average case, O(1).

3. What if elements of nums2 are stored on disk, and the memory is limited such that
you cannot load all elements into the memory at once?
ans: If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap,
read chunks of array that fit into the memory, and record the intersections.

If both nums1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort),
then read 2 elements from each array at a time in memory, record intersections.
"""