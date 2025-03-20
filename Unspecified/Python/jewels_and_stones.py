import collections

class Solution(object):
    """
    Task:
    You're given strings jewels representing the types of stones that are jewels,
    and stones representing the stones you have. Each character in stones is a type of stone you have.
    You want to know how many of the stones you have are also jewels.

    Letters are case sensitive, so "a" is considered a different type of stone from "A".
    """
    # Method 1 : using set
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        j = set(jewels)
        c = 0
        for char in stones:
            if char in j:
                c += 1
        return c


    # Method 2 : using defaultdict
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        c = collections.defaultdict(int)
        for t in jewels:
            c[t] += 0
        for t in stones:
            if t in c:
                c[t] += 1
        return sum(c.values())