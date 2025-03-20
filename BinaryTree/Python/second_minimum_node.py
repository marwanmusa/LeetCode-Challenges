import heapq
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        stack = set()
        def dfs(node):
            if node: 
                stack.add(node.val)
                print(node.val, stack)
            if node.left : dfs(node.left)
            if node.right : dfs(node.right)
        dfs(root)
        if len(stack) == 1: return -1
        a, b = heapq.nsmallest(2, stack)
        return b