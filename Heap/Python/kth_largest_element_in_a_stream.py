from heapq import heapify, heappop, heappushpop, heappush

# using heap
class KthLargest:
    """
    Task:
    Design a class to find the kth largest element in a stream. 
    Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Implement KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

    """
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.pq = nums[:min(k, len(nums))]
        heapify(self.pq)
        for i in range(k, len(nums)):
            heappushpop(self.pq, nums[i])

    def add(self, val: int) -> int:
        heappush(self.pq, val)
        if len(self.pq) > self.k: heappop(self.pq)
        return self.pq[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)