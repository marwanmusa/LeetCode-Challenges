from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        track = []
        def helper(root):
            if root:
                helper(root.left)
                track.append(root.val)
                helper(root.right)
        helper(root)
        diff = track[-1]
        for i in range(len(track)-1):
            diff = min(diff, abs(track[i]-track[i+1]))
        return diff
    
    # O(N) time complexity
    pre, cur = -float('inf'), float('inf')
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root:
            self.minDiffInBST(root.left)
            self.cur = min(self.cur, root.val-self.pre)
            self.pre = root.val
            self.minDiffInBST(root.right)
        return self.cur