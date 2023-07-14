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
    Given the root of a binary tree and an integer targetSum,
    return true if the tree has a root-to-leaf path such that
    adding up all the values along the path equals targetSum.

    A leaf is a node with no children.
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if the tree is none, there is no sum
        if root is None: return False

        ans = False
        sub_sum = targetSum - root.val

        # if the root is a leaf
        # and sub_sum is already zero 
        # then return True
        if sub_sum == 0 and root.left is None and root.right is None:
            return True

        # otherwise check for subtrees
        # as long as ans is False, function will be recurred
        # if ans is True then the answer has already been found
        if root.left != None:
            ans = ans or self.hasPathSum(root.left, sub_sum)
        if root.right != None:
            ans = ans or self.hasPathSum(root.right, sub_sum)
        return ans


    # dfs
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        self.dfs(root, targetSum, res)
        return any(res)

    def dfs(self, root, target, res):
        if root:
            if not root.left and not root.right and root.val == target:
                res.append(True)
            if root.left:
                self.dfs(root.left, target-root.val, res)
            if root.right:
                self.dfs(root.right, target-root.val, res)