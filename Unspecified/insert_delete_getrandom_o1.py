import random

# Solution 1
class RandomizedSet:
    """
    Task:
    Implement the RandomizedSet class:

    RandomizedSet() Initializes the RandomizedSet object.
    - bool insert(int val) Inserts an item val into the set if not present.
      Returns true if the item was not present, false otherwise.
    - bool remove(int val) Removes an item val from the set if present.
      Returns true if the item was present, false otherwise.
    - int getRandom() Returns a random element from the current set of elements
      (it's guaranteed that at least one element exists when this method is called).
      Each element must have the same probability of being returned.

    You must implement the functions of the class such that each function works in average O(1) time complexity.
    """
    def __init__(self):
        self.x = set()

    def insert(self, val: int) -> bool:
        if val not in self.x:
            self.x.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.x:
            return False
        self.x.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(tuple(self.x))


# Solution 2 - Optimized
class RandomizedSet:

    def __init__(self):
        self.vals = {}
        self.idxs = []

    def insert(self, val: int) -> bool:
        if val in self.vals : return False
        self.vals[val] = len(self.idxs)
        self.idxs.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.vals:
            lst = self.idxs[-1]
            pos = self.vals[val]

            self.vals[lst] = pos               # move last value to the space
            self.idxs[pos] = lst               # occupied by the queried one...

            self.vals.pop(val)                 # ...and delete the respective
            self.idxs.pop()                    # data from both structures

            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.idxs)        # as simple as that


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()