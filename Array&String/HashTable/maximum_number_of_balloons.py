from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = Counter(text)
        balloon = Counter("balloon")
        return min([word[w] // balloon[w] for w in balloon])