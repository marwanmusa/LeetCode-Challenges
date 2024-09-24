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

        def dfs(root, depth, par):
            nonlocal height
            if root:
                height[root.val] = depth
                parent[root.val] = par
                dfs(root.left, depth + 1, root.val)
                dfs(root.right, depth + 1, root.val)
        dfs(root, 0, 0)
        return height[x] == height[y] and parent[x] != parent[y]
