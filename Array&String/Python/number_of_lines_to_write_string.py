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

    # similar to prev solution
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        last, lines = 0, 1
        for w in s:
            cur = widths[ord(w)-ord('a')]
            lines += 1 if last + cur > 100 else 0
            last = cur if last + cur > 100 else last + cur
        return [lines, last]