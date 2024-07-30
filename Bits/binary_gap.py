class Solution:
    def binaryGap(self, n: int) -> int:
        one = '1'
        bin_rep = bin(n)[2:]
        cur, d = -1, 0
        if bin_rep.count(one) < 2:
            return 0
        else:
            for i in range(len(bin_rep)):
                if bin_rep[i] == one:
                    if cur < 0:
                        cur = i
                    else:
                        d = max(d, abs(i-cur))
                        cur = i
        return d