from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    Task:
    A linked list of length n is given such that each node contains an additional random pointer,
    which could point to any node in the list, or null.

    Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
    where each new node has its value set to the value of its corresponding original node.
    Both the next and random pointer of the new nodes should point to new nodes in the copied list
    such that the pointers in the original list and copied list represent the same list state.
    None of the pointers in the new list should point to nodes in the original list.

    For example, if there are two nodes X and Y in the original list, where X.random --> Y,
    then for the corresponding two nodes x and y in the copied list, x.random --> y.

    Return the head of the copied linked list.

    The linked list is represented in the input/output as a list of n nodes.
    Each node is represented as a pair of [val, random_index] where:

    - val: an integer representing Node.val
    - random_index: the index of the node (range from 0 to n-1) that the random pointer points to,
      or null if it does not point to any node.

    Your code will only be given the head of the original linked list.
    """
    # Method 1
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        # Insert each node's copy right after it
        cur = head
        while cur:
            deep_copy = Node(cur.val)
            deep_copy.next = cur.next
            cur.next = deep_copy
            cur = deep_copy.next

        # Set each copy's .random
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        # Separate the copied list from the original, (re)setting every .next
        cur = head
        deep_copy = head_copy = head.next if head else None
        while cur:
            cur.next = cur = deep_copy.next
            deep_copy.next = deep_copy = cur.next if cur else None

        return head_copy


    # Method 2, using dictionary
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nmap = dict()
        curr = head
        while curr:
            nmap[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        while curr:
            nmap[curr].next = nmap[curr.next] if curr.next else None
            nmap[curr].random = nmap.get(curr.random, None) if curr.random  else None
            curr = curr.next
        return nmap[head]