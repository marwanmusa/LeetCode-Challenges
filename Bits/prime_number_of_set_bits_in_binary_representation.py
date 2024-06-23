from collections import Counter
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prs = {x: True for x in [2, 3, 5, 7, 11, 13, 17, 19]}
        return sum([prs.get(Counter(filter(lambda x: x=='1', bin(x)))['1'], False) for x in range(left, right+1)])