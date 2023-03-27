class Solution:
    """
    Task:
    Given an integer num, return the number of steps to reduce it to zero.

    In one step, if the current number is even, you have to divide it by 2,
    otherwise, you have to subtract 1 from it.
    """
    # Method 1 using modulo
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num & 1 == 0: num >>= 1
            else: num -= 1
            steps += 1
        return steps

    # Method 2 using recursion
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return num
        return 1 + (self.numberOfSteps(num//2) if num % 2 == 0 else self.numberOfSteps(num - 1))

    # Method 3 using bitwise operators
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            # num: xxxxx0 & bitmask: 000001
            if num & 1 == 0: num >>= 1
            else: num -= 1
            steps += 1
        return steps