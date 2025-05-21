class Solution:
    """
    Task:
    Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
    """
    def addDigits(self, num: int) -> int:
        return (num-1) % 9 + 1 if num else 0