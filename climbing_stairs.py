class Solution:
    """
    Task:
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?
    """
    def climbStairs(self, n: int) -> int:
        init_val, second_val = 0, 1
        for i in range(n):
            init_val, second_val = second_val, init_val + second_val
        return second_val