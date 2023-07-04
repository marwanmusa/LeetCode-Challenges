from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Task:
    Given the root of a binary tree, return all root-to-leaf paths in any order.

    A leaf is a node with no children.
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)] + [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]