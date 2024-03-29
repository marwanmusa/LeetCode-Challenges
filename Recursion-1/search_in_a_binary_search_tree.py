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
    You are given the root of a binary search tree (BST) and an integer val.

    Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
    If such a node does not exist, return null.
    """
    # Binary search
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        while root:
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
            else:
                return root


    # recursive
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        while root:
            if val > root.val:
                return self.searchBST(root.right, val)
            elif val < root.val:
                return self.searchBST(root.left, val)
            else:
                return root