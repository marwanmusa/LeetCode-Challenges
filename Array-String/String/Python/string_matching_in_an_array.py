class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        words, res = sorted(words, key = lambda x: len(x)), []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res