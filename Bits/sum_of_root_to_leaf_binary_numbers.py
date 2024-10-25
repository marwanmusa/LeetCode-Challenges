from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        bits = defaultdict(list)
        def helper(root, h):
            if root:
                bits[h].append(root.val)
                helper(root.left, h+1)
                helper(root.right, h+1)
        helper(root, 0)
        comb_per_h = []
        for k,v in bits.items():

        return 0