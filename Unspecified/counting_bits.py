class Solution:
    """
    Task:
    Given an integer n, return an array ans of length n + 1 such that
    for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
    """
    # method 1, sum 1 bits of each i in the binary representation
    def countBits(self, n: int) -> list[int]:
        res = []
        for i in range(n+1):
            res.append(sum([int(x) for x in bin(i)[2:]]))
        return res

    # method 2, there is a pattern that
    # sum of 1 bits of each iteration follows
    # [x+1 for x in an array] with the initial value of the array is [0]
    def countBits(self, n: int) -> list[int]:
        res = [0]
        while len(res) <= n:
            res.extend([x+1 for x in res])
        return res[:n+1]