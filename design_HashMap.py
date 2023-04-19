# Using Linked-List
class ListNode(object):
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None

class MyHashMap(object):
    def __init__(self):
        self.length = 1000
        self.table = [None] * self.length


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.length
        if self.table[index] == None:
            self.table[index] = ListNode(key, value)
        else:
            curr = self.table[index]
            while True:
                if curr.pair[0] == key:
                    curr.pair = (key, value)
                    return
                if curr.next == None:
                    curr.next = ListNode(key, value)
                    return
                curr = curr.next


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % self.length
        curr = self.table[index]
        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]
            curr = curr.next
        return -1


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.length
        curr = self.table[index]
        if curr == None:
            return
        if curr.pair[0] == key:
            self.table[index] = curr.next
            return
        prev = curr
        curr = curr.next
        while curr:
            if curr.pair[0] == key:
                prev.next = curr.next
                return
            curr = curr.next
            prev = prev.next



# Using List
class MyHashMap(object):

    def __init__(self):
        self.key = []
        self.val = []

    def put(self, key, value):
        if key in self.key:
            idx = self.key.index(key)
            self.val[idx] = value
        else:
            self.key.append(key)
            self.val.append(value)


    def get(self, key):
        if key in self.key:
            idx = self.key.index(key)
            return self.val[idx]
        return -1


    def remove(self, key):
        if key in self.key:
            idx = self.key.index(key)
            self.key.pop(idx)
            self.val.pop(idx)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)