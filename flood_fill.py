from typing import List

class Solution:
    """
    Task:
    An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

    You are also given three integers sr, sc, and color.
    You should perform a flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill, consider the starting pixel,
    plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
    plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
    Replace the color of all of the aforementioned pixels with color.

    Return the modified image after performing the flood fill.
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        img_row = len(image)-1
        img_col = len(image[0])-1
        source = image[sr][sc]

        if color == source: return image

        def recursive_fill(row, col, imgGrid):
            if row < 0 or row > img_row or col < 0 or col > img_col:
                return

            if imgGrid[row][col] == source:
                imgGrid[row][col] = color

                recursive_fill(row-1, col, imgGrid) #left
                recursive_fill(row+1, col, imgGrid) #right
                recursive_fill(row, col-1, imgGrid) #top
                recursive_fill(row, col+1, imgGrid) #bottom

        recursive_fill(sr, sc, image)

        return image

    # adjustment
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curColor = image[sr][sc]
        if curColor == color :
            return image

        def dfs(x,y):
            if x<0 or y<0 or x>=len(image) or y>=len(image[0]): return
            if image[x][y] == color: return
            if image[x][y] == curColor:
                image[x][y] = color

                for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                    dfs(x+dx, y+dy)
        dfs(sr, sc)
        return image