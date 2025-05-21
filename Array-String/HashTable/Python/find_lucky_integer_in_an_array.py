from collections import defaultdict
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        n, cnt = -1, defaultdict(int)
        for x in arr:
            cnt[x] += 1
        for k in cnt:
            if k == cnt[k]: n = max(n, k)
        return n
