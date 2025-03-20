from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        height = dict()
        parent = dict()
        def dfs(root, depth, par, x, y):
            nonlocal height
            nonlocal parent
            if len(height) == 2 and len(parent) == 2:
                return
            if root:
                if root.val == x or root.val == y:
                    height[root.val] = depth
                    parent[root.val] = par
                dfs(root.left, depth + 1, root.val, x, y)
                dfs(root.right, depth + 1, root.val, x, y)
        dfs(root, 0, 0, x, y)
        return height[x] == height[y] and parent[x] != parent[y]
