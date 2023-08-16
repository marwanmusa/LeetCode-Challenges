from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # brute force
        for char in letters:
            if char > target:
                return char
        return letters[0]