class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_dict = {char: idx for idx, char in enumerate(order)}
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]) : return False
                if words[i][j] != words[i + 1][j]:
                    if order_dict[words[i][j]] > order_dict[words[i + 1][j]]: return False
                    break
        return True

    # another approach
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        mapp = {v: idx for idx, v in enumerate(order)}
        words = [[mapp[c] for c in word] for word in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

    # one-liner
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: map(order.index, w))