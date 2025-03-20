from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        vals = set()
        def helper(root, vals):
            if root:
                vals.add(root.val)
                helper(root.left, vals)
                helper(root.right, vals)
        helper(root, vals)
        return len(vals) == 1


    # shorter
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            return not node or node.val == root.val and dfs(node.left) and dfs(node.right)
        return dfs(root)