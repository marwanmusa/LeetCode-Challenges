from typing import List

class Solution:
    """
    Task:
    Write a function that reverses a string.
    The input string is given as an array of characters s.

    You must do this by modifying the input array in-place
    with O(1) extra memory.
    """
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


    # Using python built-in function
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]