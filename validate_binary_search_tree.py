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
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.
    """
    # Using stack
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        prv = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prv:
                return False
            prv = root.val
            root = root.right

        return True

    # Using recursion validate left and right subtrees
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root,float("-inf"), float("inf") )

    def validate(self, root, min_val, max_val) :
        if root is None :
            return True

        if not (min_val < root.val < max_val):
            return False

        left = self.validate(root.left, min_val, root.val)
        right = self.validate(root.right, root.val, max_val)

        return left and right