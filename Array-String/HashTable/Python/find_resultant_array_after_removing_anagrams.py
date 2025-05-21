class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        n, res = len(words), []
        prev = None
        for w in words:
            cur = sorted(w)
            if prev != cur:
                res.append(w)
                prev = cur
        return res