from typing import List

class Solution:
    """
    Task:
    Given an array of integers temperatures represents the daily temperatures,
    return an array answer such that answer[i] is the number of days you have to wait after the ith day
    to get a warmer temperature. If there is no future day for which this is possible,
    keep answer[i] == 0 instead.

    Intuition:
    Improved from the stack solution, which iterates backwards.
    We itereate forward here so that enumerate() can be used.
    Everytime a higher temperature is found, we update answer of the peak one in the stack.
    If the day with higher temperature is not found, we leave the ans to be the default 0.
    """
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0] * len(temp)
        stack = []
        for i, t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append(i)
        return ans