class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        le = len(n)
        rem = le % 3
        if le < 4: return n
        ans = n[:rem]
        r = '.'.join(n[i:i+3] for i in range(rem, le, 3))
        return f"{ans}." + r if ans else r

    # shorter
    def thousandSeparator(self, n: int) -> str:
        return '{:,}'.format(n).replace(',', '.') if n >= 0 else '-{:,}'.format(-n).replace(',', '.')

    # shorter using indexing
    def thousandSeparator(self, n: int) -> str:
        s, res = str(n), ""
        n = len(s)
        for i in range(n):
            if i > 0 and (n - i) % 3 == 0: res += "."
            res += s[i]
        return res