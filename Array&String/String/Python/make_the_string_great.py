class Solution:
    def makeGood(self, s: str) -> str:
        n, res = len(s), ""
        for c in s:
            if len(res) > 0 and abs(ord(res[-1]) - ord(c)) == 32: res = res[:-1]
            else: res += c
        return res