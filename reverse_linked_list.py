from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Task:
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Follow up:
    A linked list can be reversed either iteratively or recursively.
    Could you implement both?
    """
    # Using recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp

    # Using iteration
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_ll = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = new_ll
            new_ll = curr
            curr = next_node
        return new_ll