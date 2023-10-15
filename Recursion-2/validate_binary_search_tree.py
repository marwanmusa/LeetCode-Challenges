from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than the node's key.
        - The right subtree of a node contains only nodes with keys greater than the node's key.
        - Both the left and right subtrees must also be binary search 
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, low, high):
            if not root: return True
            if not low < root.val < high: return False
            return traverse(root.left, low, root.val) and traverse(root.right, root.val, high)

        return traverse(root, float("-inf"), float("inf"))
    
    # or we can write it,
    def isValidBST(self, root: Optional[TreeNode], lessThan = float("inf"), largerThan = float("-inf")):
        if not root : return True
        if lessThan <= root.val or root.val <= largerThan: return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))