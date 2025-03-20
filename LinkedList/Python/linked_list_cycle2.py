from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Task:
    Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
    the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
    is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

    Do not modify the linked list.
    """
    # method 1 : using Floyd’s loop detection algorithm.
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        slow = head
        fast = head

        slow = slow.next
        fast = fast.next.next

        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        if slow != fast:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    # Method 2 use hashing
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        uset = set()
        ptr = head

        while ptr != None:
            if ptr in uset:
                return ptr
            else:
                uset.add(ptr)
            ptr = ptr.next
        return None