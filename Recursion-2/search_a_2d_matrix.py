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

    # Binary search (time complexity: O(log(n)
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

    # recursive
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        O(log(mn)) time, O(logmn) space, because we discard 1/4 of the matrix each time.

        Recursive binary search midpoint of matrix. Given co-ordiantes (r_low, r_high, c_low, c_high)
        inclusive of a square submatrix, and midpoint r_mid=r_low+(r_high-r_low)//2, c_mid=c_low+(c_high-c_low)//2,

        Use helper function search(r_low, r_high, c_low, c_high) on the co-ordinates of a sub-matrix

        1. Check (r_low, r_high, c_low, c_high) is valid, i.e. 0<=r_low<=r_high<=R-1, 0<=c_low<=c_high<=C-1.
        If not return False.
        2. If matrix[r_mid][c_mid]==target, return True
        3. Elif matrix[r_mid][c_mid]>target, discard the bottom right portion including matrix[r_mid][c_mid], 
        i.e. search for target in the tree subtricies:
        (r_low, r_mid-1, c_low, c_mid), (r_low, r_mid-1, c_mid+1, c_high), (r_mid, r_high, c_low, c_mid-1)
        return True if any return true.
        4. Elif matrix[r_mid][c_mid]<target, discard top left corner, search for
        (r_low, r_mid, c_mid+1, c_high), (r_mid+1, r_high, c_mid, c_high), (r_mid+1, r_high, c_low, c_mid-1)
        return True if any return true.
        """
        R,C=len(matrix), len(matrix[0])

        def search_sub(r_low, r_high, c_low, c_high):
            if not (0<=r_low<=r_high<=R-1) or not (0<=c_low<=c_high<=C-1):
                return False
            r_mid=r_low+(r_high-r_low)//2
            c_mid=c_low+(c_high-c_low)//2
            if matrix[r_mid][c_mid]==target:
                return True

            elif matrix[r_mid][c_mid]>target: #discard bottom right
                tl=(r_low, r_mid-1, c_low, c_mid)
                tr=(r_low, r_mid-1, c_mid+1, c_high)
                bl=(r_mid, r_high, c_low, c_mid-1)

                return search_sub(*tl) or search_sub(*tr) or search_sub(*bl)
            elif matrix[r_mid][c_mid]<target: #discard top left
                tr=(r_low, r_mid, c_mid+1, c_high)
                br=(r_mid+1, r_high, c_mid, c_high)
                bl=(r_mid+1, r_high, c_low, c_mid-1)

                return search_sub(*tr) or search_sub(*br) or search_sub(*bl)

        return search_sub(0, R-1, 0, C-1)
    
    # Linear Search from Top-Right Corner
    def searchMatrix(matrix, target):
        m, n = len(matrix), len(matrix) and len(matrix[0])
        r, c = 0, n-1
        while r < m and c >= 0:
            if target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
            else: return True
        return False