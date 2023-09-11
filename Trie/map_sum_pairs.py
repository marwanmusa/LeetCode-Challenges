# Map Sum Pairs
"""
Design a map that allows you to do the following:
    - Maps a string key to a given value.
    - Returns the sum of the values that have a key with a prefix equal to a given string.

Implement the MapSum class:
    - MapSum() Initializes the MapSum object.
    - void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed,
      the original key-value pair will be overridden to the new one.
    - int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
"""

from collections import Counter


# Approach 1: Brute-Force
class MapSum(object):
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        return sum(val for key, val in self.map.items()
                   if key.startswith(prefix))
    
# Approach 2: Prefix Hashmap
class MapSum(object):
    def __init__(self):
        self.map = {}
        self.score = Counter()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        for i in range(len(key) + 1):
            prefix = key[:i]
            self.score[prefix] += delta
    
    def sum(self, prefix):
        return self.score[prefix]
    
# Approach 3: Trie
class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):
    def __init__(self):
        self.map = {}
        self.root = TrieNode()
    
    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta
    
    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score