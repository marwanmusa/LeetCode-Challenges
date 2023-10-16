class Solution:
    """
    Task:
    You are given an m x n integer matrix matrix with the following two properties:
    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the previous row.

    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.
    """
    # Method 1 (time complexity: On))
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        for i in range(m):
            if target in matrix[i]:
                return True
        return False

    # Method 2 (adjustment from above method) (time complexity: O(n))
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                return target in row
        return False

    # 1 Binary search (time complexity: O(log(n)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        start = 0
        end = row*col - 1

        mid = start + (end-start)//2

        while start <= end:
            x  = matrix[mid//col][mid%col]

            if x == target:
                return True

            if x < target:
                start = mid + 1
            else:
                end = mid - 1

            mid = start + (end-start)//2

        return False
