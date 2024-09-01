from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def helper(root):
            nonlocal ans
            if root:
                if low <= root.val <= high:
                    ans += root.val
                helper(root.left)
                helper(root.right)
        helper(root)
        return ans
    
    # without helper
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
    
    # shorter
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        return (root.val if low <= root.val <= high else 0) + \
                self.rangeSumBST(root.left, low, high) +\
                self.rangeSum(root.right, low, high)