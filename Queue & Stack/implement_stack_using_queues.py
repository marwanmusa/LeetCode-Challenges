"""
Task:
    Implement a last-in-first-out (LIFO) stack using only two queues.
    The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

    Implement the MyStack class:
        - void push(int x) Pushes element x to the top of the stack.
        - int pop() Removes the element on the top of the stack and returns it.
        - int top() Returns the element on the top of the stack.
        - boolean empty() Returns true if the stack is empty, false otherwise.

    Notes:
        - You must use only standard operations of a queue, which means that only push to back,
          peek/pop from front, size and is empty operations are valid.
        - Depending on your language, the queue may not be supported natively.
          You may simulate a queue using a list or deque (double-ended queue)
          as long as you use only a queue's standard operations.

    Follow-up: Can you implement the stack using only one queue?
"""
import collections
# Approach 1 (One Queue, push-O(n), pop-O(1))
class MyStack:
    def __init__(self):
        self._queue = collections.deque()

    def push(self, x: int) -> None:
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self) -> int:
        return self._queue.popleft()

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return not self._queue


# Approach 2 (Two Queues, push-O(n), pop-O(1))
class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        while self.queue1:
            self.queue2.append(self.queue1.pop())
        self.queue1.append(x)
        while self.queue2:
            self.queue1.append(self.queue2.pop())

    def pop(self) -> int:
        return self.queue1.pop(0)

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()