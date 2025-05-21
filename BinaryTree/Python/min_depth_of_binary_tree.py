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
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path
    from the root node down to the nearest leaf node.

    Note: A leaf is a node with no children.
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        elif root.left is None and root.right is None: return 1

        if root.left is None:
            return self.minDepth(root.right)+1

        if root.right is None:
            return self.minDepth(root.left)+1

        return min(self.minDepth(root.left), self.minDepth(root.right))+1