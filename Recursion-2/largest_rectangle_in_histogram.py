class Solution:
    """
    Task:
        Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
        return the area of the largest rectangle in the histogram.
    """
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        stack = [-1]  # use -1 as a placeholder for the upper limit
        max_area = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        heights.pop()
        return max_area