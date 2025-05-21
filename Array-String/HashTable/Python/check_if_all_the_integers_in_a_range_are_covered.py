class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        mp = [False for _ in range(right-left+1)]
        for r in ranges:
            start, end = max(r[0], left), min(r[1]+1, right+1)
            for i in range(start, end):
                mp[i - left] = True
        return all(mp)
