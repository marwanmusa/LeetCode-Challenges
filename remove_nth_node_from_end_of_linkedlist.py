from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Task:
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    """
    # method 1
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while right and n>0:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next


    # method 2
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return

        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head