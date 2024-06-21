import collections
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        lp = collections.Counter([x for x in licensePlate if x.isalpha()])
        cur = 0
        for i, x in enumerate(words):
            if 