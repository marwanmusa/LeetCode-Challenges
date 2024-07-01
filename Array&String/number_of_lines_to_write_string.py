class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        last, lines = 0, 0
        for w in s:
            cur = widths[ord(w)-ord('a')]
            if last + cur > 100:
                lines += 1
                last = 0
            last += cur
        return [lines+1, last]