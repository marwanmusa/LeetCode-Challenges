class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = deque([])
        n = len(s)
        dash = '-'
        cur = 0
        for i in range(n - 1, -1, -1):
            print(i, s[i])
            if s[i] != dash:
                if cur < k:
                    res.appendleft((s[i]).upper())
                    cur += 1
                elif cur == k-1 and i != 0:
                    res.appendleft(dash)
                    cur -= k
        return "".join(res)