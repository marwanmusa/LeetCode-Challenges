# Implement Trie (Prefix Tree)
"""
A trie (pronounced as "try") or prefix tree is a tree data structure
used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the trie
      (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously inserted string word
      that has the prefix prefix, and false otherwise.
"""

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word
        
    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)