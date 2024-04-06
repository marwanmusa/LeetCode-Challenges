from collections import defaultdict
from typing import Optional

"""
Task:
    Given the root of a binary search tree (BST) with duplicates, return all the mode(s)
    (i.e., the most frequently occurred element) in it.

    If the tree has more than one mode, return them in any order.

    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        arr, stack, d = [], [root], defaultdict(int)

        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            arr.append(cur.val)

        for el in arr:
            d[el] += 1

        maxval = d[max(d, key=d.get)]
        ans = [k for k,v in d.items() if v == maxval]
        return sorted(ans)
    
    # shorter version
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        arr, stack, d = [], [root], defaultdict(int)
        while stack:
            cur = stack.pop()
            if cur.left: stack.append(cur.left)
            if cur.right:stack.append(cur.right)
            d[cur.val] += 1
        return sorted([k for k,v in d.items() if v == max(d.values())])