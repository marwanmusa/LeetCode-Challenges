class Solution:
    """
    Task:
    We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
    Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01,
    and each occurrence of 1 with 10.

    For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
    Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
    """
    # recursion with index and level
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: # base case
            return 0

        else: # general case
            if k % 2 == 0:
                # even index of current level is opposite of parent level's [(K+1)//2]
                return 1 - self.kthGrammar(n-1, (k+1)//2)
            else:
                # odd index of current level is same as parent level's [(k+1)//2]
                return self.kthGrammar(n-1, (k+1)//2)


    # by the rule of output
    def kthGrammar(self, n: int, k: int) -> int:
        """
        Observation:

        Output value is decided by the number of 1s in binary representation of (K-1)

        If binary representation of K-1 has odd 1s, then output value is 1
        If binary representation of K-1 has even 1s, then output value is 0
        """
        return bin(k-1).count('1') % 2