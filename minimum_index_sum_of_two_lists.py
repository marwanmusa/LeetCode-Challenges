from collections import defaultdict
from typing import List

class Solution:
    """
    Task:
    Given two arrays of strings list1 and list2, find the common strings with the least index sum.
    A common string is a string that appeared in both list1 and list2.
    A common string with the least index sum is a common string
    such that if it appeared at list1[i] and list2[j]
    then i + j should be the minimum value among all the other common strings.

    Return all the common strings with the least index sum.
    Return the answer in any order.
    """
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        worddict = defaultdict(int)
        res_dict = defaultdict(int)
        for idx, word in enumerate(list1):
            worddict[word] += idx
        for idx, word in enumerate(list2):
            if word in worddict:
                res_dict[word] += worddict[word] + idx
        minval = min(res_dict.values())
        return [word for word, val in res_dict.items() if val == minval]
