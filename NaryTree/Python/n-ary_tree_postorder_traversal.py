"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if not root: return []
        stack, ans = [root], []
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            stack.extend(cur.children)
        return ans[::-1]

    # recursive
    def postorder(self, root: 'Node') -> list[int]:
        if not root: return []
        ans = []
        for child in root.children:
            ans.extend(self.postorder(child))
        ans.append(root.val)
        return ans