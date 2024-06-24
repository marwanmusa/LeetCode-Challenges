from collections import Counter
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prs = {x: True for x in [2, 3, 5, 7, 11, 13, 17, 19]}
        return sum([prs.get(bin(x).count('1'), False) for x in range(left, right+1)])

    # using bit shifting
    def countPrimeSetBits(self, L, R):
        return sum(665772 >> bin(i).count('1') & 1 for i in range(L, R+1))
