from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        cnt = sorted(list(item) for item in Counter(nums).items())
        prev = cnt[0][1]
        cnt[0][1] = 0
        for i in range(1, len(cnt)):
            cur = cnt[i][1]
            cnt[i][1] = prev
            prev += cur
        cnt = dict(cnt)
        return [cnt[x] for x in nums]
