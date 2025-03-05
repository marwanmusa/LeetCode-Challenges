"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        if not root: return []
        stack, ans = [root], []
        while stack:
            cur = stack.pop()
            if cur :
                stack.extend(reversed(cur.children))
                ans.append(cur.val)
        return ans