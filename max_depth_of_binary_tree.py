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
        if root is None: return 0
        elif root.left == root.right == None: return 1
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return 1 + ((right_depth, left_depth)[left_depth, right_depth])