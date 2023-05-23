from collections import deque
class Solution:
    """
    Task:
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
    return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.
    """
    def numIslands(self, grid):
        count = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    queue.append((i,j))
                    self.helper(grid,queue) # turn the adjancent '1' to '0'
                    count += 1
        print(grid)
        return count

    def helper(self,grid,queue):
        while queue:
            I,J = queue.popleft()
            for i,j in [I-1,J],[I+1,J],[I,J-1],[I,J+1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    queue.append((i,j))
                    grid[i][j] = 0


# Intuition by zhanweiting
"""
In the grid, we need to record 1 peice of information of one point, grid[i][j], i.e., if grid[i][j] has been visited or not.
We initialize the check matrix with all False. It means none of the elements in the check matrix has been visited.
If one point grid[i][j] has not been visited, check[i][j] == False, it means we haven't count this point into one islands.
If one point grid[i][j] has been visited, check[i][j] == True, it means we already count this point into one islands.

Search function:
Each time you call search function, the search function will end
until all the neighbors of grid[i][j] have value "1" been visited, i.e.,
those points are labeled True in check matrix.


Example:
grid = [ 1 ,  1 ,  1,
		 1,   1,   0,
		 0,   0,   1]
		 
Intial check:
check = [ False, False, False,
		  False, False, False,
		  False, False, False]
		  
# the first time call  search function:
grid[0][0] == '1' and check[0][0] == False:
check = [ True, True, True,
		  True, True, False,
		 False, False, False ]
count = 1
# the second time call check function:
grid[2][2] = '1' and check[2][2] == False:
check = [ True, True, True,
		  True, True, False,
		 False, False, True]
Count = 2


Improve space complexity to O(1):
we can improve the algorithm by replacing the check matrix by flip the visited '1' to '0'.
We can flip the visited '1' to '0' since we are only adding the index of '1' into the queue.
The connected '1' already flip into '0', so we don't need to worry about duplicate calculation.
"""