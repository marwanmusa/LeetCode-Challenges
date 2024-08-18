import math

from collections import Counter
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        cnt = Counter(deck).values()
        return reduce(gcd, cnt) > 1
    
    # one line
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        return reduce(math.gcd, Counter(deck).values()) > 1