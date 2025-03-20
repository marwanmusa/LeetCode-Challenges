from collections import defaultdict

class Solution:
    # using hashmap
    def greatestLetter(self, s: str) -> str:
        letters = defaultdict(set)
        pos = []
        for char in s:
            curLetter = char.lower()
            letters[curLetter].add(char)
            if len(letters[curLetter]) > 1: pos.append(curLetter.upper())
        return max(pos) if pos else ''

    # using string manipulation
    def greatestLetter(self, s: str) -> str:
        for i in range(25, -1, -1):
            low, up = chr(97 + i), chr(65 + i)
            if low in s and up in s:
                return up
        return ''