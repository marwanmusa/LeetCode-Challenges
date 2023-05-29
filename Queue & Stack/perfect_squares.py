class Solution:
    """
    Task:
    Given an integer n, return the least number of perfect square numbers that sum to n.
    A perfect square is an integer that is the square of an integer; in other words,
    it is the product of some integer with itself.
    For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
    """
    # Using BFS
    def numSquares(self, n: int) -> int:
        if n < 2: return n

        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1

        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y: return cnt
                    if x < y: break
                    temp.add(x-y)
            toCheck = temp

        return cnt