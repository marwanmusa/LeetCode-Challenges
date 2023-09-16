"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure, it can be matched later.
    - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
      word may contain dots '.' where dots can be matched with any letter.
 
"""

# Using SET
class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        cur = self.d
        if not self.search(word):
            for i in range(len(word)):
                if word[i] not in cur:
                    cur[word[i]] = {}
                cur = cur[word[i]]
            cur['#'] = {}

    def search(self, word: str) -> bool:
        cur = self.d
        def rec(start, cur):
            if start >= len(word):
                return True if '#' in cur else False
        
            if word[start] == '.':
                for k,v in cur.items():
                    if rec(start+1, v):
                        return True
                return False
            elif word[start] in cur:
                if rec(start+1, cur[word[start]]):
                    return True
            else:
                return False
        return rec(0, cur)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Using TRIE
class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word):
        cur_node = self.root
        for char in word :
            cur_node = cur_node.children.setdefault(char, TrieNode())
        cur_node.is_word = True

    def search(self, word):
        def dfs(trie , index ):
            if index == len(word):
                return trie.is_word
            
            if word[index] == '.':
                for child in trie.children.values():
                    if dfs(child, index+1):
                        return True
            
            if word[index] in trie.children:
                return dfs(trie.children[word[index]], index+1)
            return False
        
        return dfs(self.root, 0)