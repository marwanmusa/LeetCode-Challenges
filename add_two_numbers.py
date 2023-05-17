from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    # Method 1
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        res_tail = res
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 +val2 + carry, 10)

            res_tail.next = ListNode(out)
            res_tail = res_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return res.next


    # Method 2
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
        Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list,
        which contains the least-significant digit.

        Args:
            l1 (Optional[ListNode]): _description_
            l2 (Optional[ListNode]): _description_

        Returns:
            Optional[ListNode]: _description_
        """

        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next