class MyCircularQueue:
    """
    Task:
    Design your implementation of the circular queue.
    The circular queue is a linear data structure in which the operations are performed
    based on FIFO (First In First Out) principle, and the last position is connected
    back to the first position to make a circle. It is also called "Ring Buffer".

    One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
    In a normal queue, once the queue becomes full, we cannot insert the next element
    even if there is a space in front of the queue. But using the circular queue,
    we can use the space to store new values.

    Implement the MyCircularQueue class:

    - MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    - int Front() Gets the front item from the queue. If the queue is empty, return -1.
    - int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    - boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    - boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    - boolean isEmpty() Checks whether the circular queue is empty or not.
    - boolean isFull() Checks whether the circular queue is full or not.

    You must solve the problem without using the built-in queue data structure in your programming language.
    """
    def __init__(self, k: int):
        self.k = k
        self.q = [None]*k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail =(self.tail+1)%self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.head] = None
        self.head = (self.head+1)%self.k
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[self.tail-1]

    def isEmpty(self) -> bool:
        return self.head == self.tail and not self.q[self.head]

    def isFull(self) -> bool:
        return self.tail ==  self.head and self.q[self.head]



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()