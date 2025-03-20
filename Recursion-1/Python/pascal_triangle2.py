"""
Task:
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
"""
from typing import List
class Solution:
    # Method I - recursion
    def getRow(self, rowIndex: int) -> List[int]:
        target_row = []
        target_row.append(1)

        # return target row = [1] as initiate val of pascal's triangle
        if rowIndex == 0:
            return target_row

        # do recursive, get target row based on prev row
        prev = self.getRow(rowIndex - 1)

        for i in range(1, len(prev)):
            curr = prev[i-1]+prev[i]
            target_row.append(curr)
        target_row.append(1)
        return target_row

    # Method II
    def getRow(self, rowIndex: int) -> List[int]:
        target_row = [1]
        prev = 1
        for i in range(1, rowIndex+1):
            curr = (prev*(rowIndex-i+1))//i
            target_row.append(curr)
            prev = curr
        return target_row
