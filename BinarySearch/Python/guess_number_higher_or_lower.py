# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    """
    Task:
    We are playing the Guess Game. The game is as follows:

    I pick a number from 1 to n. You have to guess which number I picked.

    Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

    You call a pre-defined API int guess(int num), which returns three possible results:
        -1: Your guess is higher than the number I picked (i.e. num > pick).
        1: Your guess is lower than the number I picked (i.e. num < pick).
        0: your guess is equal to the number I picked (i.e. num == pick).

    Return the number that I picked.
    """
    def guessNumber(self, n: int) -> int:
        lo, hi = 0, n
        if guess(lo) == 0:
            return lo
        while lo <= hi:
            pick = lo + (hi - lo)//2
            if guess(pick) == 0:
                return pick
            elif guess(pick) == -1:
                hi = pick - 1
            else:
                lo = pick +1
        return -1