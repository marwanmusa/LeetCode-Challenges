from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Task:
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path
    from the root node down to the farthest leaf node.
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)

    # or simply
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # bottom-up solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        elif root.left == root.right == None: return 1
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return 1 + (right_depth, left_depth)[left_depth>right_depth]

    # top-down solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def top_down(root: Optional[TreeNode], depth: int):
            if not root: return
            if not root.left and not root.right:
                self.ans = max(self.ans, depth)
            top_down(root.left, depth +1)
            top_down(root.right, depth + 1)
        top_down(root, 1)
        return self.ans