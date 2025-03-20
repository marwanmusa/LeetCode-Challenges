from typing import List

class Solution:
    """
    Task:
    Write a function that reverses a string.
    The input string is given as an array of characters s.

    You must do this by modifying the input array in-place
    with O(1) extra memory.
    """
    # classic
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


    # Using python built-in function / pythonic
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


    # recursively
    def reverseString(self, s: List[str]) -> List[str]:
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])

    def reverseString(self, s: List[str]) -> None:
        def helper( left:int, right:int, string: List[str]):
            if left >= right:
                # base case
                return
            # general case
            s[left], s[right] = s[right], s[left]
            helper( left+1, right-1, s)
        # ------------------------------------------------
        helper( left = 0, right = len(s)-1, string = s)