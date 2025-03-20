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
    Given an integer array nums where the elements are sorted in ascending order,
    convert it to a height-balanced binary search tree.
    """
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # set median arr as root
        mid = (len(nums))//2
        root = TreeNode(nums[mid])

        #left subtree of root : val < nums[mid]
        root.left = self.sortedArrayToBST(nums[:mid])

        #right subtree of root : val > nums[mid]
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    # extra function for displaying PreOrder Traversal of constructed BST
    def preOrder(self, node : Optional[TreeNode]):
        if not node:
            return None
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)
