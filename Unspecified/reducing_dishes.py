from typing import List

class Solution:
    """
    Task:
    A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

    Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes
    multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

    Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

    Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
    """
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        n = len(satisfaction)
        presum, res = 0, 0
        for i in range(n):
            presum += satisfaction[i]
            if presum < 0:
                break
            res += presum
        return res