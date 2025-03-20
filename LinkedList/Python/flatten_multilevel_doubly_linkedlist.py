from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    """
    Task:
    You are given a doubly linked list, which contains nodes that have a next pointer,
    a previous pointer, and an additional child pointer.
    This child pointer may or may not point to a separate doubly linked list,
    also containing these special nodes. These child lists may have one or more children of their own,
    and so on, to produce a multilevel data structure as shown in the example below.

    Given the head of the first level of the list,
    flatten the list so that all the nodes appear in a single-level, doubly linked list.
    Let curr be a node with a child list. The nodes in the child list should appear after curr
    and before curr.next in the flattened list.

    Return the head of the flattened list.
    The nodes in the list must have all of their child pointers set to null.
    """
    # Method 1
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        cur = head

        while cur:
            if cur.child == None:
                cur = cur.next
            else:
                tail_child = cur.child

                while tail_child.next:
                    tail_child = tail_child.next
                tail_child.next = cur.next

                if tail_child.next:
                    tail_child.next.prev = tail_child
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None
        return head


    # Method 2
    def flatten(self, h: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(h, t=None):
            if not h:
                return t
            h.next = dfs(h.child, dfs(h.next, t))
            if h.next:
                h.next.prev = h
            h.child = None
            return h
        return dfs(h)