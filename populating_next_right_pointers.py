import collections
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    Task:
    You are given a **perfect binary tree** where all leaves are on the same
    level, and every parent has two children. The binary tree has the following
    definition:

        struct Node {int val;
                    Node *left;
                    Node *right;
                    Node *next;}

    Populate each next pointer to point to its next right node. If there is no
    next right node, the next pointer should be set to `NULL`.

    Initially, all next pointers are set to `NULL`.
    """
    # Using BFS
    def connect(self, node: Optional[Node]) -> Optional[Node]:
        cur, nxt = node, node.left if node else None

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return node

    # Using queue
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root: return None

        q = collections.deque()
        q.append(root)

        while q:
            count = len(q)

            for i in range(count):
                node = q.popleft()
                if i!= count - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root