from typing import List

class Solution:
    # brute force
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for char in letters:
            if char > target:
                return char
        return letters[0]
    

    # binary search
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s = -1
        e = len(letters) - 1
        while s+1 < e:
            m = (s + e)//2
            if letters[m] > target:
                e = m
            else:
                s = m
        return letters[e] if letters[e] > target else letters[0]