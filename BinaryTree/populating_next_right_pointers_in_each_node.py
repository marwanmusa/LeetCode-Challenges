from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # bfs - right to left
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                cur = q.popleft()
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    q.extend([cur.right, cur.left])
        return root

    # dfs
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        L, R, N = root.left, root.right, root.next
        if L:
            L.next = R
            if N: R.next = N.left
            self.connect(L)
            self.connect(R)
        return root

    # bfs space-optimized approach
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = root
        while root:
            cur, root  = root, root.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next: cur.right.next = cur.next.left
                else: break
                cur = cur.next
        return head