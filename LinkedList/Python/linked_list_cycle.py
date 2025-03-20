from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Task:
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again
    by continuously following the next pointer. Internally, pos is used to denote the index of the node
    that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_push = head
        fast_push = head
        while slow_push and fast_push and fast_push.next:
            slow_push = slow_push.next
            fast_push = fast_push.next.next
            if slow_push == fast_push:
                return True
        return False