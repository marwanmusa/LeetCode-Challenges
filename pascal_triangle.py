from typing import List

class Solution:
    """
    Task:
    Given an integer numRows, return the first numRows of Pascal's triangle.
    """
    def generate(self, numRows: int) -> List[List[int]]:
        numSeries = [[1]]
        if numRows == 1:
            return numSeries
        else:
            for i in range(1, numRows):
                arr = []
                arr.append(1)
                for j in range(1, len(numSeries[i-1])):
                    arr.append(numSeries[i-1][j-1]+numSeries[i-1][j])
                arr.append(1)
                numSeries.append(arr)
        return numSeries