# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original: return None
        if original == target: return cloned
        r = self.getTargetCopy(original.right, cloned.right, target)
        if r: return r
        return self.getTargetCopy(original.left, cloned.left, target)


    #  another implementation
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(o: TreeNode, c: TreeNode) -> None:
            if o:
                helper(o.left, c.left)
                if o is target: self.ans = c
                helper(o.right, c.right)
        helper(original, cloned)
        return self.ans