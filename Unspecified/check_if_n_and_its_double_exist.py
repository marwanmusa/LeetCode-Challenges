from typing import List

class Solution:
    """
    Task:
    Given an array arr of integers, check if there exist two indices i and j such that :
        - i != j
        - 0 <= i, j < arr.length
        - arr[i] == 2 * arr[j]
    """
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for n in arr:
            if n * 2 in seen or n / 2 in seen:
                return True
            seen.add(n)
        return False