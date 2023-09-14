import collections
from functools import reduce

class Solution:
    """
    In English, we have a concept called root, which can be followed by some other word
    to form another longer word - let's call this word successor. 
    For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

    Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
    replace all the successors in the sentence with the root forming it. 
    If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

    Return the sentence after the replacement.
    """
    # Approach 1: Prefix Hash
    # For each word in the sentence, we'll look at successive prefixes and see if we saw them before
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        rootset = set(dictionary)

        def replace(word):
            for i in range(len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word
        
        return " ".join(map(replace, sentence.split()))
    
    # Approach 2: Trie
    # Put all the roots in a trie (prefix tree). Then for any query word,
    # we can find the smallest root that was a prefix in linear time.
    def replaceWords(self, roots: list[str], sentence: str) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))
    
    # another form of approach 2
    def replaceWords(self, roots: list[str], sentence: str) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            cur = trie
            for letter in root:
                cur = cur[letter]
            cur[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur: break
                cur = cur[letter]
                if END in cur:
                    return cur[END]
            return word
        
        return " ".join(map(replace, sentence.split()))