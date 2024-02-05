from collections import defaultdict
from typing import List

class Solution:
    """
    Task:
    Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
    return the number of tuples (i, j, k, l) such that:

    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
    """
    # Method 1
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sums, res = defaultdict(int), 0
        for x in nums1:
            for y in nums2:
                sums[x + y] += 1

        for i in nums3:
            for j in nums4:
                res += sums[0 - (i + j)]

        return res


    # Method 2
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        def count_each_possible_sum(lists):
            res = defaultdict(int)
            for val in lists[0]:
                res[val] += 1

            for l in lists[1:]:
                new_res = defaultdict(int)
                for val in l:
                    for prev_sum in res:
                        new_res[prev_sum+val] += res[prev_sum]
                res = new_res
            return res


        def get_num_of_tuples(all_lists, target):
            num_of_lists = len(all_lists)
            left_counter = count_each_possible_sum(all_lists[:num_of_lists//2])
            right_counter = count_each_possible_sum(all_lists[num_of_lists//2:])
            res = 0
            for right_key in right_counter:
                left_key = target-right_key
                if left_key in left_counter:
                    res += right_counter[right_key]*left_counter[left_key]
            return res

        return get_num_of_tuples([nums1, nums2, nums3, nums4], 0)