class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, w in enumerate(sentence.split()):
            if w.find(searchWord) == 0: return i + 1
        return -1