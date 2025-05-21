from collections import deque
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Return the length of the shortest path between root and target node.
def bfs(root: Optional[ListNode], target: Optional[ListNode]) -> int:
    queue = deque()     # store all nodes which are waiting to be processed
    visited = set()     # store all the nodes that we've visited
    step = 0            # number of steps needed from root to current node

    # Initialize
    queue.append(root)
    visited.add(root)

    # BFS
    while queue is not None:
        # iterate the nodes which are already in the queue
        size = len(queue)
        for i in range(size):
            cur = queue.popleft()
            if cur == target:
                return step
            while cur.next:
                if cur.next not in visited:
                    queue.append(cur.next)
                    visited.add(cur.next)
                cur = cur.next
            step += 1
    return -1   # there is no path from root to target