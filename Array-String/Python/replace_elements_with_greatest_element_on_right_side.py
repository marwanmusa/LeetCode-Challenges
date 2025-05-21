from typing import List

class Solution:
    """
    Task:
    Given an array arr, replace every element in that array with the greatest element among the elements to its right,
    and replace the last element with -1.

    After doing so, return the array.
    """
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = 0
        cur = 0
        for i in reversed(range(0, len(arr)-1)):
            max_ = max(arr[i+1], cur)
            cur = arr[i]
            arr[i] = max(cur, max_)
        arr.pop(0)
        arr.append(-1)
        return arr


    # More efficient way
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = arr[-1]
        arr[-1] = -1
        for i in range(0, len(arr)-1)[-1::-1]:
            temp = current_max
            if current_max < arr[i]:
                current_max = arr[i]
            arr[i] = temp
        return arr