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

    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []
        n = len(heights)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                hp, ip = stack.pop()
                max_area = max(max_area, hp * (i - ip))
                start = ip
            stack.append((h, start))
        for h, i in stack:
            max_area = max(max_area, h * (n - i))
        return max_area
    
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack, max_area = [], 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area